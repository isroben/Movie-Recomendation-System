import ast
import sys
from sklearn.base import BaseEstimator, TransformerMixin
from src.utils.logger import get_logger
from src.utils.exception import CustomException
import pandas as pd



class BaseTransformer(BaseEstimator, TransformerMixin):
    """Inherit from this instead of sklearn directly.
    Guarantees your transform() always receives a clean DataFrame."""

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = pd.DataFrame(X).copy()
        return self._transform(X)

    def _transform(self, X):
        raise CustomException(Exception, sys)
    

class ListConverter(BaseTransformer):
    def _transform(self, X):

        converted = X.apply(lambda col: col.map(self._convert))
        return converted.apply(lambda row: sum(row.tolist(), []), axis=1).values

    def _convert(self, obj):
        L = []
        for i in ast.literal_eval(obj):
            L.append(i['name'])
        return L


class FetchCasts(BaseTransformer):
    def _transform(self, X):
        # X is guaranteed to be a DataFrame here ✅
        ...

class FetchDirs(BaseTransformer):
    def _transform(self, X):
        # X is guaranteed to be a DataFrame here ✅
        ...

class ReplaceSpaces(BaseTransformer):
    def _transform(self, X):
        # X is guaranteed to be a DataFrame here ✅
        ...