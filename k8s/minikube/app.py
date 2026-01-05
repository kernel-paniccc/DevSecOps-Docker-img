from datetime import datetime
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

GREETING = "hello from Flask"


@app.get("/")
def index():
    return jsonify(message=GREETING, ts=datetime.utcnow().isoformat() + "Z")


@app.get("/health")
def healthz():
    return "ok", 200


@app.post("/echo")
def echo():
    payload = request.get_json(silent=True) or {}
    return jsonify(echo=payload, ip=request.remote_addr)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
