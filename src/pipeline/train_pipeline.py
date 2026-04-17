import sys
import os
from src.utils.exception import CustomException
from src.utils.logger import get_logger

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
# from src.components.model_trainer import ModelTrainer

logger = get_logger(__name__)

def training_pipeline():
    try:
        logger.info("Training Pipeline started.")

        # Data Ingestion
        ingestion = DataIngestion()
        movies, credits = ingestion.initiateDataIngestion()

        logger.info("Data ingetion completed.")

        # Data Transformation
        transform = DataTransformation()
        transform.initiateDataTransformation(movies, credits)

        
        logger.info("Data transformation completed.")

    except Exception as e:
        raise CustomException(e,sys)
    
training_pipeline()