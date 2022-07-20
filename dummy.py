import os,sys

from pip import main
from housing.component.data_transformation import DataTransformation
from housing.logger import logging
from housing.exception import ExceptionHendler
from housing.pipeline.pipeline import Pipeline
from housing.config.configuration import Configuration
from numpy import dtype
from housing.component.data_ingestion import DataIngestion

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        #data_transformation = DataTransformation(data_ingestion_artifact=data_ingest)
        #print(data_transformation)
        logging.info("demo class has been created and logging and exception test started")
    except Exception as e:
        housing_exception = ExceptionHendler(e,sys)
        logging.info("This is a Demo to test")

if __name__=="__main__":
    main()