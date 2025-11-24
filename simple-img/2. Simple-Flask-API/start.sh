#!/bin/bash

DIR="$(dirname "$0")"

# Build the Docker image
docker build -t simple-flask-api "$DIR"

# Run the Docker container
docker run -d -p 5000:5000 --name simple-flask-app simple-flask-api

echo "Flask API is running on http://localhost:5000"
