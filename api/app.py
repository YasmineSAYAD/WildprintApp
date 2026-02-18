
import json
import os
import sqlite3
from sqlite3 import Connection

import numpy as np
from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from PIL import Image
from tensorflow.keras.models import load_model

app = Flask(__name__)
app.secret_key = "iqusgdoiqzgdpaohbpng$p^zoepobng,^pozpebngnôpzen,gn^bopzne,p"
CORS(app, resources={
    r"/*": {"origins": "http://localhost:8080"}
})

#allowed extensions for loaded track image
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# db connection
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "wildprint.db")
def get_db_connection()-> Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# page test
@app.route("/", methods=["GET"])
def home() -> str:
    return "API Flask ✅"

# ---------------predictions------------------------

# load CNN
model = load_model("api/model.keras")

# load class names
try:
    with open("class_names.json") as f:
        class_names = json.load(f)
except Exception as e:
    class_names = []
    print("Erreur lors du chargement des classes :", e)

# allowed images extension
def allowed_file(filename: str) -> bool:
    return (
        '.' in filename and
        filename.rsplit('.', 1)[1].lower()
        in app.config['ALLOWED_EXTENSIONS']
    )

# predict
@app.route('/predict', methods=['POST'])
def predict() -> Response:
    # check that image is present in files
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}, 400)

    file = request.files['image']

    # if file name is not empty
    if not file.filename or file.filename is None:
        return jsonify({"error": "No image selected"}, 400)

    # check that image file is present
    if file and allowed_file(file.filename):
        try:
            #image preprocessing
            img = Image.open(file.stream).convert("RGB")
            img = img.resize((256, 256))
            image_array = np.array(img)
            image_array = np.expand_dims(image_array, axis=0)

            # Prediction
            prediction = model.predict(image_array)
            predicted_index = int(np.argmax(prediction[0]))

            # check index
            if predicted_index >= len(class_names):
                return jsonify(
                    {
                        "error": "Predicted index exceeds class_names length",
                        "predicted_index": predicted_index,
                        "class_names_length": len(class_names),
                    }
                    , 500
                )

            # get class label
            predicted_label = class_names[predicted_index]

            # find animal in db
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM animals WHERE species = ?",
                (predicted_label,)
            )
            row = cursor.fetchone()

            # if animal not found
            if row is None:
                return jsonify({"error": "animal not found"}, 404)

            conn.close()
            return jsonify({"animal": dict(row)})

        except Exception as e:
            return jsonify({"error": f"Unexpected error: {str(e)}"}, 500)


    return jsonify({"error": "Invalid file type"}, 400)


# ---------------tracks------------------------
# save track
@app.route("/tracks", methods=["POST", "GET"])
def tracks() -> Response:
    # connection db
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        new_track = request.get_json()
        # verify missing data
        missing = [key for key in ["loc", "date", "species"] if not new_track.get(key)]
        if missing:
            return jsonify({"error": "missing data " + ', '.join(missing)}, 400)

        try:
            # insert track
            cursor.execute(
                """
                INSERT INTO tracks (path, loc, date, animal_sp)
                VALUES (?, ?, ?, ?)
                """,
                (
                    "track.jpg",
                    new_track["loc"],
                    new_track["date"],
                    new_track["species"],
                ),
            )
            conn.commit()
            conn.close()
            return jsonify({"message": "track added successfully"}, 201)

        except Exception as e:
            return jsonify({"error": "Unexpected error " + str(e)}, 500)

    elif request.method == "GET":
        cursor.execute("SELECT * FROM tracks")
        rows = cursor.fetchall()
        conn.close()
        return jsonify([dict(row) for row in rows], 200)

    return jsonify({"error": "Method Not Allowed"}, 405)

# ---------------animals------------------------
@app.route("/animals", methods=["Get"])
def animals()-> Response:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animals")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return jsonify([dict(row) for row in rows], 200)
