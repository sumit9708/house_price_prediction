import os,sys
from tkinter import E
from housing.constant import *
from housing.logger import logging
from housing.exception import ExceptionHendler
import yaml
from housing.entity.config_entity import DataIngestionConfig, DataTransformationConfig \
                      , DataValidationConfig, ModelEvaluationConfig, ModelPusherConfig, ModelTrainerConfig, TrainingPipelineConfig
from housing.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from housing.util.util import read_yaml_file

class Configuration:
    def __init__(self,config_file_path:str =CONFIG_FILE_PATH,
                     current_time_stamp:str = CURRENT_TIME_STAMP
      )->None:
        try:
            logging.info("Data entry start for reading yaml file")
            self.config_info = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
            logging.info("Data has been imported from yaml file to configuration class successfuly")
        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            logging.info("Started data ingestion process")
            artifact_dir = self.training_pipeline_config.artifact_dir

            data_ingestion_artifact_dir = os.path.join(artifact_dir,
            DATA_INGESTION_ARTIFACT_DIR_NAME,
            self.time_stamp
            )

            data_ingestion_config = self.config_info[DATA_INGESTION_CONFIG_KEY]

            dataset_download_url = data_ingestion_config[DATA_INGESTION_DATASET_DOWNLOAD_URL_KEY]

            tgz_download_dir = os.path.join(data_ingestion_artifact_dir,
            data_ingestion_config[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]
            )

            raw_data_dir = os.path.join(data_ingestion_artifact_dir,
            data_ingestion_config[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )

            ingested_dir = os.path.join(data_ingestion_artifact_dir,
            data_ingestion_config[DATA_INGESTION_INGESTED_DIR_KEY]
            )

            ingested_train_dir = os.path.join(data_ingestion_artifact_dir,
            data_ingestion_config[DATA_INGESTION_INGESTED_DIR_KEY],
            data_ingestion_config[DATA_INGESTION_INGESTED_TRAIN_DIR_KEY]
            )

            ingested_test_dir = os.path.join(data_ingestion_artifact_dir,
            data_ingestion_config[DATA_INGESTION_INGESTED_DIR_KEY],
            data_ingestion_config[DATA_INGESTION_INGESTED_TEST_DIR_KEY]
            )
            logging.info("data ingestion configuration started")

            data_ingestion_config = DataIngestionConfig(
                dataset_download_url,
                raw_data_dir,
                tgz_download_dir,
                ingested_dir,
                ingested_train_dir,
                ingested_test_dir
            )
            logging.info("Data ingestion completed successfuly")

            return data_ingestion_config
    
        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def get_data_validation_config(self,data_ingestion_artifact:DataIngestionArtifact)->DataValidationConfig:
        try:
            logging.info("-----------Data Validation log Started--------------")
            self.data_Ingestion_artifact = data_ingestion_artifact
            training_pipeline_config = self.get_training_pipeline_config()
            data_validation_config = self.config_info[DATA_VALIDATION_CONFIG_KEY]

            logging.info(f"data validation config is : {data_validation_config}")

            artifact_dir = self.training_pipeline_config.artifact_dir

            data_validation_artifact_dir = os.path.join(artifact_dir,
                                              DATA_VALIDATION_ARTIFACT_DIR_NAME,
                                              self.time_stamp)

            logging.info(f"Data validation Arifact Directory is : {data_validation_artifact_dir}")

            schema_file_name = data_validation_config[DATA_VALIDATION_SCHEMA_FILE_NAME]

            schema_file_path = os.path.join(data_validation_artifact_dir,schema_file_name)


            
            logging.info(f"Data validation Schema file is : {schema_file_name}")
            report_file_name = data_validation_config[DATA_VALIDATION_REPORT_FILE_NAME]
            logging.info(f"report file name is : {report_file_name}")

            report_file_path = os.path.join(data_validation_artifact_dir,report_file_name)

            report_page_file_name = data_validation_config[DATA_VALIDATION_REPORT_PAGE_FILE_NAME]

            logging.info(f"report page file name is : {report_page_file_name}")

            report_page_file_path = os.path.join(data_validation_artifact_dir,report_page_file_name)

            data_validation_config = DataValidationConfig(
                schema_file_path, 
                report_file_path, 
                report_page_file_path)

            logging.info("------------------Data Validation Configuration Completed-----------------")

            return data_validation_config
            logging.info(f" Data validation Config is : {data_validation_config}")

        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def get_data_transformation_config(self)->DataTransformationConfig:
        pass

    def get_model_trainer_config(self)->ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self)->ModelPusherConfig:
        pass

    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            logging.info("Training pipeline configuration started")
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
                                        training_pipeline_config[PIPELINE_NAME],
                                        training_pipeline_config[ARTIFACT_DIR]
                                        )

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"training pipeline configguration is:{training_pipeline_config}")
            return training_pipeline_config

        except Exception as e:
            raise ExceptionHendler(e,sys) from e





