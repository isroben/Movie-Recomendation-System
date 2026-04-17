import sys
import os
from dataclasses import dataclass
import pandas as pd
import ast

from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

ps = PorterStemmer()

from src.utils.exception import CustomException
from src.utils.logger import get_logger


logger = get_logger(__name__)

@dataclass
class DataTransformationConfig():
    preprocessorObj_path = os.path.join('artifacts', 'preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()

    def getTransformationObj(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)
    

    def transform(df):
        # drop nulls
        df = df.dropna().copy()

        # extract
        df['genres']   = df['genres'].apply(lambda x: [i['name'] for i in ast.literal_eval(x)])
        df['keywords'] = df['keywords'].apply(lambda x: [i['name'] for i in ast.literal_eval(x)])
        df['cast']     = df['cast'].apply(lambda x: [i['name'] for i in ast.literal_eval(x)[:3]])
        df['crew']     = df['crew'].apply(lambda x: [i['name'] for i in ast.literal_eval(x) if i['job'] == 'Director'])
        df['overview'] = df['overview'].apply(lambda x: x.split() if isinstance(x, str) else [])

        # remove spaces
        for col in ['genres', 'keywords', 'cast', 'crew']:
            df[col] = df[col].apply(lambda words: [w.replace(" ", "") for w in words])

        # combine into tags
        df['tags'] = df['genres'] + df['keywords'] + df['overview'] + df['cast'] + df['crew']

        # stem
        df['tags'] = df['tags'].apply(lambda words: [ps.stem(w) for w in words])

        # join to string
        df['tags'] = df['tags'].apply(lambda x: " ".join(x)).str.lower()

        # final clean dataframe
        df = df[['id', 'title', 'tags']]

        # vectorize
        cv = CountVectorizer(max_features=5000, stop_words='english')
        vectors = cv.fit_transform(df['tags']).toarray()

        return df, vectors, cv


