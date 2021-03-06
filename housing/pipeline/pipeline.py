from housing.component.data_transformation import DataTransformation
from housing.component.data_validation import DataValidation
from housing.config.configuration import Configuration
from housing.constant import *
from housing.exception import ExceptionHendler
import os,sys
from housing.logger import logging
from housing.component.data_ingestion import DataIngestion

from housing.entity.artifact_entity import DataIngestionArtifact, DataTransformationArtifact, DataValidationArtifact, ModelTrainerArtifact
from housing.entity.config_entity import DataIngestionConfig, DataTransformationConfig,DataValidationConfig, ModelTrainerConfig
from housing.component.data_validation import DataValidation
from housing.component.data_transformation import DataTransformation
from housing.component.model_trainer import ModelTraining

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

    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:
        try:
        
            logging.info("----------------Pipeline Log Started------------------")
            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                            data_ingestion_artifact=data_ingestion_artifact
        )
            
            return data_validation.initiate_data_validation()
            logging.info("-------------------Data Validation Started-------------------")
        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def start_data_transformation(self,data_ingestion_artifact:DataIngestionArtifact,
                                  data_validation_artifact:DataValidationArtifact,
                                  data_transformation_config:DataTransformationConfig
        )->DataTransformationArtifact:
        try:

            config = Configuration()

            data_transformation = DataTransformation(config,data_ingestion_artifact=data_ingestion_artifact,
                                data_transformation_config=data_transformation_config,
                                data_validation_artifact=data_validation_artifact
            )

            return data_transformation.initiate_data_transformation()
        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def start_model_training(self,data_transformation_artifact:DataTransformationArtifact)->ModelTrainerArtifact:
        try:
            logging.info("-----------model training log inside pipeline started------------------")
            model_trainer_config = self.config.get_model_trainer_config()
            self.data_transformation_artifact = data_transformation_artifact

            model_training = ModelTraining(data_transformation_artifact=data_transformation_artifact,model_training_config=model_trainer_config)

            logging.info("---------------model training log inside pipeline is completed---------------")

            return model_training.initiate_model_training()
        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def run_pipeline(self):
        try:
            # Data Ingestion
            logging.info("-----------------run pipeline function log started--------------------")
            config = Configuration()
            data_transformation_config = config.get_data_transformation_config()
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(
                data_transformation_config= data_transformation_config,
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_artifact=data_validation_artifact)

            model_trainer_artifact = self.start_model_training(data_transformation_artifact=data_transformation_artifact)

            logging.info(f"data ingestion artifact : {data_ingestion_artifact} and data validation artifact is :{data_validation_artifact} and data transformation artifact is ;[{data_transformation_artifact}]")
            return data_ingestion_artifact,data_validation_artifact,data_transformation_artifact,model_trainer_artifact

        except Exception as e:
            raise ExceptionHendler(e,sys) from e