from flask import Flask, request, jsonify
from redis import Redis
import uuid, os

app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route("/upload", methods=["POST", "GET"])
def upload_document():
    file_path = "dummy_text.txt"
    # file = request.files["file"]
    document_id = str(uuid.uuid4())
    file = open(file_path, "rb")
    with open(file_path, "wb") as f:
        f.write(file.read())
    redis.lpush("documents", document_id)
    return jsonify(
        {"message": "Document uploaded successfully", "document_id": document_id}
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
