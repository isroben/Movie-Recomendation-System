import os
import sys

import pandas as pd
from dataclasses import dataclass

from src.utils.exception import CustomException
from src.utils.logger import get_logger

logger = get_logger(__name__)

@dataclass
class DataIngestionCofig:
    movies_data_path : str = r"data/raw/tmdb_5000_movies.csv"
    credits_data_path : str = r"data/raw/tmdb_5000_credits.csv"


class DataIngestion:
    def __init__(self):
        self.config = DataIngestionCofig()

    def initiateDataIngestion(self):
        logger.info("Staring data ingestion process.")

        try:
            if not os.path.exists(self.config.movies_data_path):
                raise CustomException(f"Source data file doesn't exist: {self.config.movies_data_path}", sys)
            if not os.path.exists(self.config.credits_data_path):
                raise CustomException(f"Source data file doesn't exist: {self.config.credits_data_path}", sys)
            
            # Loading dataset
            movies = pd.read_csv(self.config.movies_data_path)
            credits = pd.read_csv(self.config.credits_data_path)
            logger.info("Dataset loaded successfully.")

            return movies, credits
        
        except Exception as e:
            raise CustomException(e, sys)

            