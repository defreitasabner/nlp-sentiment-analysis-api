from flask import request, jsonify

from main import app
from services import SentimentAnalysisService

sentiment_analysis_service = SentimentAnalysisService()

@app.route("/")
def home():
    return "Send a POST request with a field 'text' containing a string!"

@app.route("/", methods=["POST"])
def predict_polarity():
    input_data = request.get_json()
    prediction = sentiment_analysis_service.predict_polarity(input_data["text"])
    response = {"prediction": prediction[0]}
    return jsonify(response)