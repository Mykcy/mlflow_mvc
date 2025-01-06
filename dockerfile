# Stage 1: Build React App
FROM node:14 AS react-build
WORKDIR /app
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Build Flask App
FROM python:3.8-slim AS flask-build
WORKDIR /app
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ ./

# Stage 3: Final Image
FROM python:3.8-slim
WORKDIR /app

# Copy Flask app
COPY --from=flask-build /app /app

# Copy React build
COPY --from=react-build /app/build /app/static

# Install MLflow
RUN pip install mlflow

# Expose ports
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
