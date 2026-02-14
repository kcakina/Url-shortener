from flask import Flask, request, jsonify
from app.db import DB
from app.services import assign_short_url

app = Flask(__name__)
db = DB()
COUNTER = 0


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/urls", methods=["POST"])
def create_url():
    global COUNTER
    body = request.get_json()
    if not body or "url" not in body:
        return jsonify({"error": "missing 'url' field"}), 400

    result = assign_short_url(db, body["url"], COUNTER)
    if result is None:
        return jsonify({"error": "failed to create short url"}), 500

    COUNTER += 1
    return jsonify({
        "id": result.shortUrl,
        "shortUrl": f"/u/{result.shortUrl}"
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)