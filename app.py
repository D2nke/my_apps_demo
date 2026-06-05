from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/")
def home():
    return jsonify(message="my_apps_demo - Python branch")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
