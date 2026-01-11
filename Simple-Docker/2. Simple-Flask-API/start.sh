#!/bin/bash

DIR="$(dirname "$0")"

docker build -t simple-flask-api "$DIR"

docker run -d -p 5000:5000 --name simple-flask-app simple-flask-api

echo "http://localhost:5000"
