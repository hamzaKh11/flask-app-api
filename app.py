from flask import Flask, jsonify, request
from transformers import pipeline

app = Flask(__name__)

# Explicitly load the pre-trained sentiment-analysis model and tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)

# Define the prediction endpoint


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "No text field in request"}), 400

    text = data['text']
    # Get the sentiment prediction
    result = sentiment_analyzer(text)[0]

    # Return the result as a JSON response
    return jsonify({
        "label": result['label'],  # positive/negative
        "confidence": result['score']  # confidence score
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
