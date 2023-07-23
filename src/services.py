from typing import List
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

from helpers import DataTreater

class SentimentAnalysisService:
    def __init__(self) -> None:
        self.__model: LogisticRegression = pickle.load(open('./src/models/model.sav', 'rb'))
        self.__vectorizer: CountVectorizer = pickle.load(open('./src/models/vectorizer.sav', 'rb'))
        self.__data_treater = DataTreater()

    def predict_polarity(self, input_data: str):
        treated_data = self.__data_treater.treat_input_data(input_data)
        bag_of_words = self.__generate_bag_of_words(treated_data)
        return self.__model.predict(bag_of_words)
   
    def __generate_bag_of_words(self, data: str):
        return self.__vectorizer.transform([data])