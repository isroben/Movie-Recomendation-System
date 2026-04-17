import os
import sys
from dataclasses import dataclass
import pandas as pd
from sqlalchemy import create_engine

from src.utils.exception import CustomException
from src.utils.logger import get_logger

logger = get_logger(__name__)

@dataclass
class DataIngestionConfig:
    db_user: str = 'postgres'
    db_password: str = "Letmein$$"
    db_host: str = "localhost"
    db_port : str = "5432"
    db_name : str = "tmdt_movie_dataset"

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def _get_engine(self):
        try:
            connection_string = (
                f"postgresql://{self.config.db_user}:"
                f"{self.config.db_password}@"
                f"{self.config.db_host}:"
                f"{self.config.db_port}/"
                f"{self.config.db_name}"
            )

            engine = create_engine(connection_string)
            logger.info("PostgresSQL connection established.")
            
            return engine
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiateDataIngestion(self):
        try:
            logger.info("Data Ingestion started.")

            engine = self._get_engine()

            query = """
            SELECT * FROM movies
            """

            dataset = pd.read_sql(query, engine)

            logger.info(f"Dataset loaded succesfully. Shape: {dataset.shape}")

            return dataset
        
        except Exception as e:
            raise CustomException(e, sys)


dataObj = DataIngestion()
dataset = dataObj.initiateDataIngestion()
print(dataset.head())
print("called obj")