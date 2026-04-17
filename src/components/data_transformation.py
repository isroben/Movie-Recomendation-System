import sys
import os
from dataclasses import dataclass
import pandas as pd
import ast

from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer


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

    def initiateDataTransformation(self, movies, credits):
        try:
            df = pd.merge(movies, credits, on='title')
            print(df.columns)

            dataset = df[['id', 'genres', 'title', 'keywords', 'overview', 'cast', 'crew']]

            dataset.dropna(inplace=True)

            movie_id = dataset['id'].values
            movie_title = dataset['title'].values

        except Exception as e:
            raise CustomException(e, sys)

