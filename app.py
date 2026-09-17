"""
app.py
Flask backend for the Fake News Detection web app.
"""

import os
import joblib
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

MODEL_PATH = os.path.join("model", "model.pkl")
VECTORIZER_PATH = os.path.join("model", "vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()

    if not text:
        return jsonify({"error": "Please enter some text to analyze."}), 400

    if len(text.split()) < 3:
        return jsonify({"error": "Please enter a longer piece of text (at least a few words)."}), 400

    vect_text = vectorizer.transform([text])
    prediction = model.predict(vect_text)[0]

    score = model.decision_function(vect_text)[0]
    confidence = min(99.0, 50 + abs(score) * 10)

    return jsonify({
        "prediction": prediction,
        "confidence": round(confidence, 1)
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)