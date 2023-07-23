from typing import List
import string

import unidecode
import nltk

class DataTreater:
    def __init__(self) -> None:
        self.__tokenizer = nltk.tokenize.WordPunctTokenizer()
        self.__stemmer = nltk.RSLPStemmer()
        self.__stopwords_puncts: List[str] = self.__get_portuguese_stopwords_punctuation_list()

    def treat_input_data(self, input_data: str) -> str:
        tokenized_data: List[str] = self.__tokenizer.tokenize(input_data)
        treated_data = []
        for token in tokenized_data:
            treated_token = unidecode.unidecode(token.lower())
            if treated_token not in self.__stopwords_puncts:
                treated_data.append(self.__stemmer.stem(treated_token))
        return ' '.join(treated_data)

    def __get_portuguese_stopwords_punctuation_list(self) -> List[str]:
        portuguese_stopwords = \
            list(set([ unidecode.unidecode(stopword) for stopword in nltk.corpus.stopwords.words("portuguese") ]))
        punctuation = [ punct for punct in string.punctuation ]
        return sorted(portuguese_stopwords + punctuation)