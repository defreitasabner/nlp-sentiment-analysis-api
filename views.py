from helpers import DataTreater
from main import app
from flask import request

@app.route("/")
def home():
    return "Hello World!"

@app.route("/", methods=["POST"])
def treat_data():
    input_data = request.get_json()
    data_treater = DataTreater()
    return data_treater.treat_input_data(input_data["text"])