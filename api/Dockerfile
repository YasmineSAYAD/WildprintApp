# =================== Stage 1: Builder ====================
FROM python:3.11.9-slim AS builder

WORKDIR /app/api

COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

# ================== Stage 2: Final image ====================
FROM python:3.11.9-slim

WORKDIR /app

# Copy installed packages
COPY --from=builder /install /usr/local

# Copy your API code into /app/api
COPY . /app

# Flask environment variables
ENV FLASK_APP=api/app.py
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]