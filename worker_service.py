from flask import Flask, jsonify
from redis import Redis
import time

app = Flask(__name__)
redis = Redis(host="redis", port=6379)


def count_words(document_id, k):
    with open(f"{document_id}.txt", "r") as file:
        content = file.read()
        words = content.split()
        count = sum(len(word) == k for word in words)
        return count


@app.route("/process", methods=["POST", "GET"])
def process_documents():
    document_id = redis.rpop("documents")
    if not document_id:
        return jsonify({"message": "No documents to process"})

    document_id = document_id.decode("utf-8")
    k = 5  # Specify the desired word length here
    count = count_words(document_id, k)
    result = {"document_id": document_id, "word_count": count}

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
