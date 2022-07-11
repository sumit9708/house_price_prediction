import os,sys
from datetime import datetime

ROOT_DIR = os.getcwd()
CONFIG_DIR_NAME = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR_NAME,CONFIG_FILE_NAME)
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

## Constant for Training Pipeline
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
PIPELINE_NAME = "pipeline_name"
ARTIFACT_DIR = "artifact_dir"

## Data Ingestion Constants:-

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR_NAME = "data_ingestion"
DATA_INGESTION_DATASET_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_KEY = "ingested_dir"
DATA_INGESTION_INGESTED_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_INGESTED_TEST_DIR_KEY = "ingested_test_dir"

## Data Validation Constants:-

DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIDATION_ARTIFACT_DIR_NAME = "data-validation"
DATA_VALIDATION_SCHEMA_DIR_KEY = "schema_dir"
DATA_VALIDATION_SCHEMA_FILE_NAME = "schema_file_name"
DATA_VALIDATION_REPORT_FILE_NAME = "report_file_name"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME = "report_page_file_name"

