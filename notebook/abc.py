dataset_download_url = self.data_ingestion_config.dataset_download_url

            tgz_download_dir= self.data_ingestion_config.tgz_download_dir

            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)

            os.makedirs(tgz_download_dir,exist_ok=True)

            housing_file_name = os.path.basename(dataset_download_url)

            tgz_file_path = os.path.join(tgz_download_dir,housing_file_name)

            urllib.request.urlretrieve(dataset_download_url,tgz_file_path)
            logging.info(f"file: [{tgz_file_path}] has been downloaded successfully.")
            
            return tgz_file_path


def __init__(self,data_ingestion_config:DataIngestionConfig):

        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise ExceptionHendler(e,sys) from e



import os,sys
from housing.constant import *

#from housing.constant import DATA_INGESTION_DATASET_DOWNLOAD_URL_KEY
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig
from housing.logger import logging
from housing.exception import ExceptionHendler
from six.moves import urllib
import tarfile
from housing.config.configuration import Configuration
from sklearn.model_selection import StratifiedShuffleSplit
import pandas as pd
import numpy as np


