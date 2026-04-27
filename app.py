from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["prompt"]

    r = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}]
        }
    )

    return jsonify(r.json())

@app.route("/image", methods=["POST"])
def image():
    prompt = request.json["prompt"]

    r = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers=headers,
        json={
            "prompt": "ultra realistic " + prompt,
            "size": "1024x1024"
        }
    )

    return jsonify(r.json())

app.run(host="0.0.0.0", port=5000)
