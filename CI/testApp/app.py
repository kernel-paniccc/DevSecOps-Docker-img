from flask import Flask, jsonify, request


app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(message="Hello from CI test app!")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/echo")
def echo():
    message = request.args.get("msg", "")
    payload = {"echo": message, "length": len(message)}
    if not message:
        payload["error"] = "msg query param is required"
        return jsonify(payload), 400
    return jsonify(payload)


if __name__ == "__main__":
    app.run(debug=True)
