from flask import Flask
import nltk

nltk.download('all')

app = Flask(__name__)

from views import *

if __name__ == "__main__":
    app.run(debug=True)