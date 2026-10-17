
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Lab 10 DevOps Pipeline Application",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/tasks")
def tasks():
    return jsonify([
        {"id": 1, "task": "Write application code", "completed": True},
        {"id": 2, "task": "Run automated tests", "completed": False},
        {"id": 3, "task": "Deploy using Docker", "completed": False}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
