import os,sys
from housing.logger import logging
from housing.exception import ExceptionHendler
from housing.config.configuration import Configuration
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.entity.config_entity import DataIngestionConfig
from housing.constant import *
from six.moves import urllib
import tarfile
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):

        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20}")
            self.data_ingestion_config = data_ingestion_config
            logging.info("Data Ingestion Config file imported sucsessfully")
        except Exception as e:
            raise ExceptionHendler(e,sys) from e


    def download_dataset_from_url(self)->str:

        try: 
            logging.info(f"started extrecting dataset url")
            ## Extrecting remote url to download dataset
            download_url = self.data_ingestion_config.dataset_download_url

            logging.info(f"dataset_download_url is : [{download_url}]")

            ## folder location to download file

            tgz_download_dir= self.data_ingestion_config.tgz_download_dir

            logging.info(f"tgz_download_dir is : [{tgz_download_dir}]")

            #if os.path.exists(tgz_download_dir):

                #os.remove(tgz_download_dir)

            os.makedirs(tgz_download_dir,exist_ok=True)

            housing_file_name = os.path.basename(download_url)

            tgz_file_path = os.path.join(tgz_download_dir,housing_file_name)

            logging.info(f"downloading file from: [{download_url}] into directory: [{tgz_file_path}]")

            urllib.request.urlretrieve(download_url,tgz_file_path)
            logging.info(f"file: [{tgz_file_path}] has been downloaded successfully.")

            return tgz_file_path

        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def extrected_data_ingestion_tgz_file(self):
        try:
            logging.info(f"{'='*20}dataset extrection from tgz_file started.{'='*20}")
            tgz_file_path = self.download_dataset_from_url()
            raw_data_dir = self.data_ingestion_config.raw_data_dir

            #if os.path.exists(raw_data_dir):
               # os.remove(raw_data_dir)           
            os.makedirs(raw_data_dir,exist_ok=True)

            with tarfile.open(tgz_file_path) as downloaded_dataset:
                downloaded_dataset.extractall(path=raw_data_dir)
            logging.info(f"extrected dataset has been stored succesfuly at : {raw_data_dir}")

            return raw_data_dir
        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def split_into_train_and_test(self)->DataIngestionArtifact:

        try:
            logging.info(f"{'='*20}Dataset split log started.{'='*20}")
            raw_data_dir = self.extrected_data_ingestion_tgz_file()

            file_name = os.listdir(raw_data_dir)[0]

            #os.makedirs(file_name,exist_ok=True)

            file_path = os.path.join(raw_data_dir,file_name)

            logging.info(f"raw data dir path is : [{file_path}]")

            
            ingested_data_frame = pd.read_csv(file_path)

            ingested_data_frame["income_category"] = pd.cut(ingested_data_frame["median_income"],
                                                            bins=[0,1.5,3.0,4.5,6.0,np.inf],
                                                            labels=[1,2,3,4,5]
                                                            )

            logging.info("new column created for statified split")

            ingested_train_set = None
            ingested_test_set = None                                                

            split = StratifiedShuffleSplit(n_splits=1,test_size=0.20,random_state=42)

            for train_index,test_index in split.split(ingested_data_frame,ingested_data_frame["income_category"]):
                ingested_train_set=ingested_data_frame.loc[train_index].drop("income_category",axis = 1)
                ingested_test_set = ingested_data_frame.loc[test_index].drop("income_category",axis=1)

            train_file_path = os.path.join(self.data_ingestion_config.ingested_train_dir,file_name)

            logging.info(f"training file path is : [{train_file_path}]")
            test_file_path = os.path.join(self.data_ingestion_config.ingested_test_dir,file_name)
            logging.info(f"test file path is : [{test_file_path}]")

            if ingested_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                ingested_train_set.to_csv(train_file_path,index=False)

            if ingested_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok=True)
                ingested_test_set.to_csv(test_file_path,index=False)

            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path,
                test_file_path,
                is_ingested=True, 
                message = f"Data Ingestion completed successfully"
                )

            return data_ingestion_artifact





        except Exception as e:
            raise ExceptionHendler(e,sys) from e


    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            tgz_file_path = self.download_dataset_from_url()
            raw_data_dir = self.extrected_data_ingestion_tgz_file()
            return self.split_into_train_and_test()
        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def __del__(self):
        logging.info(f"{'='*20}Data Ingestion log completed.{'='*20} \n\n")