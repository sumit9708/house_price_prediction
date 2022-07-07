import os,sys
from housing.constant import *
from housing.logger import logging
from housing.exception import ExceptionHendler
import yaml
from housing.entity.config_entity import DataIngestionConfig, DataTransformationConfig \
                      , DataValidationConfig, ModelEvaluationConfig, ModelPusherConfig, ModelTrainerConfig, TrainingPipelineConfig

from housing.util.util import read_yaml_file

class Configuration:
    def __init__(self,config_file_path:str =CONFIG_FILE_PATH,
                     current_time_stamp:str = CURRENT_TIME_STAMP
      ):
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

    def get_data_validation_config(self)->DataValidationConfig:
        pass

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
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
                                        training_pipeline_config[PIPELINE_NAME],
                                        training_pipeline_config[ARTIFACT_DIR]
                                        )

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            return training_pipeline_config

        except Exception as e:
            raise ExceptionHendler(e,sys) from e





