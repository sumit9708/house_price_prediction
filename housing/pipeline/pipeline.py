from housing.config.configuration import Configuration
from housing.constant import *
from housing.exception import ExceptionHendler
import os,sys
from housing.logger import logging
from housing.component.data_ingestion import DataIngestion

from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig
#from housing.component.data_validation import DataValidation
#from housing.component.data_transformation import DataTransformation

class Pipeline:
    def __init__(self,config: Configuration = Configuration())->None:
        try:
            self.config = config

        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def run_pipeline(self):
        try:
            # Data Ingestion
            data_ingestion_artifact = self.start_data_ingestion()
            #data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            #data_transformation_artifact = self.start_data_transformation(
                #data_ingestion_artifact=data_ingestion_artifact,
                #data_validation_artifact=data_validation_artifact
            #)
            return data_ingestion_artifact

        except Exception as e:
            raise ExceptionHendler(e,sys) from e