WildAIPrint — README

📌 Présentation du projet

WildAIPrint est une application permettant d’identifier une empreinte animale à partir d’une image.
Elle combine :

un modèle TensorFlow pour la classification d’empreintes,

une API Flask pour la prédiction et la gestion des données,

une base SQLite contenant les informations sur les espèces,

un frontend web simple et intuitif,

une dockerisation complète pour faciliter le déploiement.

L’utilisateur charge une image → l’API prédit l’espèce → le frontend affiche la fiche détaillée → l’observation est enregistrée dans la base.

🗂️ Architecture du proje

```text
wildaiprintApp/
│
├── api/
│ ├── app.py # API Flask
│ ├── model.keras # Modèle TensorFlow
│ ├── class_names.json # Labels du modèle
│ ├── infos_especes.csv # Données des espèces
│ ├── wildprint.db # Base SQLite
│ ├── requirements.txt # Dépendances Python
│ └── Dockerfile # Dockerfile de l’API
│
├── frontend/
│ ├── index.html
│ ├── script.js
│ ├── styles.css
│ └── Dockerfile
│
└── docker-compose.yml # Orchestration multi‑conteneurs
```

🚀 Fonctionnement de l’application
🔍 1. Prédiction d’une empreinte
L’utilisateur charge une image depuis le frontend.

Le frontend envoie l’image à l’API via /predict.

L’API :

charge le modèle TensorFlow,

prédit l’espèce,

récupère les informations correspondantes dans SQLite,

renvoie un objet JSON :

```json
{
  "animal": {
    "species": "Coyote",
    "name": "Canis latrans",
    "description": "...",
    "region": "...",
    "picture": "coyote.jpg"
  }
}
```

Le frontend affiche la fiche de l’animal.

📝 2. Enregistrement d’une observation
Après la prédiction, le frontend envoie :

```json
{
  "loc": "GPS ou texte",
  "date": "2026-02-03T14:00:00Z",
  "species": "Coyote"
}
```

à l’endpoint :

POST /tracks

L’API enregistre l’observation dans la table tracks.

🐳 Dockerisation

L’application utilise deux conteneurs :

flask_api → API Flask + modèle + SQLite

wildaiprint_front → frontend web

Le tout est orchestré via docker-compose.

▶️ Lancer l’application

```bash
docker-compose up --build
```

Puis ouvrir :

http://localhost

🐳 Publication de l’image sur DockerHub

1. Connexion

```bash
docker login
```

2. Tag de l’image

image front

```bash
docker tag wildaiprintapp-front yasminesayad/wildaiprintapp-front:latest
```

image API

```bash
docker tag wildaiprintapp-front yasminesayad/wildaiprintapp-front:latest
```

3. Push

image front

```bash
docker push yasminesayad/wildaiprintapp-front:latest
```

image API

```bash
docker push yasminesayad/wildaiprintapp-front:latestt
```

4. Pull depuis n’importe quelle machine

image front

```bash
docker pull yasminesayad/wildaiprintapp-front:latest
```

image API

```bash
docker pull yasminesayad/wildaiprintapp-front:latestt
```

🧪 Endpoints de l’API

🔹 GET /
Retourne un message simple pour vérifier que l’API fonctionne.

🔹 POST /predict
Envoie une image → renvoie l’espèce prédite + infos.

🔹 POST /tracks
Enregistre une observation dans SQLite.

🛠️ Technologies utilisées
Python 3.11

Flask

TensorFlow

SQLite

Docker & Docker Compose

HTML / CSS / JavaScript

👩‍💻 Auteur
Projet réalisé par Yasmine SAYAD dans le cadre du brief Dockerisation d’Application : Du Développement au Déploiement.
