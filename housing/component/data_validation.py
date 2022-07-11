from cgi import test
import logging
import os
from tkinter import E

from evidently import dashboard
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from housing.entity.config_entity import DataValidationConfig
from housing.exception import ExceptionHendler
from housing.constant import *
from housing.config.configuration import Configuration
from housing.component.data_ingestion import DataIngestion
from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
import json
import pandas as pd
import numpy as np


class DataValidation:
    def __init__(self,data_validation_config:DataValidationConfig,data_ingestion_artifact:DataIngestionArtifact)->DataValidationArtifact:

        try:

            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def get_train_df_and_test_df(self):
        try:


            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            train_df = pd.read_csv(train_file_path)
            test_df = pd.read_csv(test_file_path)

            return train_df,test_df

        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def validate_dataset_schema(self):
        try:

            Validation_status = False
            ## Check Total Numeber of Columns
            
            train_df,test_df = self.get_train_df_and_test_df()

            Number_of_columns = train_df.shape[1]

            ## Check Numerical Columns and Categorical_column

            Numerical_Columns = [feature for feature in train_df.columns if train_df[feature].dtypes !="O"]

            Categorical_Columns = [feature for feature in train_df.columns if train_df[feature].dtypes =="O"]

            ## Column Names 

            column_names = train_df.columns

            ## Values of Ocean Proximity Values

            ocean_proximity_values = train_df["ocean_proximity"].value_counts()

            Validation_status = True

            message = print(f"""Total Number Of Columns = [{Number_of_columns}]
            Columns Names are : [{column_names}],
            Numerical Feature Columns :[{Numerical_Columns}],
            Categorical Features Column : [{Categorical_Columns}],
            Values in Ocean Proximity Column : [{ocean_proximity_values}]
            Validation Status =[{Validation_status}]
            """)

            return message

        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def is_train_and_test_file_exist(self)->bool:
        try:
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path =self.data_ingestion_artifact.train_file_path

            is_train_file_exist = os.path.exists(train_file_path)

            test_file_path = self.data_ingestion_artifact.test_file_path

            is_test_file_exist = os.path.exists(test_file_path)

            is_avalibale = is_train_file_exist and is_test_file_exist

            logging.info(f"Is train and test file exist : [{is_avalibale}]")

            if not is_avalibale:
                training_file = os.path.exists(self.data_ingestion_artifact.train_file_path)
                test_file = os.path.exists(self.data_ingestion_artifact.test_file_path)
                message =print(f"Train File:[{training_file} and Test File:[{test_file}] is not available]")
                raise Exception(message)

            return is_avalibale

        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def get_and_save_data_drift_report(self):
        try:
            logging.info("----------Get Report Log Started-------------")
            profile = Profile(sections=[DataDriftProfileSection()])
            train_df,test_df = self.get_train_df_and_test_df()
            profile.calculate(train_df,test_df)
            report = json.loads(profile.json())
            logging.info(f"report is : {report}")
            report_file_path = self.data_validation_config.report_file_path
            
            report_dir = os.path.dirname(report_file_path)
            logging.info(f"report dir is :{report_dir}")
            os.makedirs(report_dir,exist_ok=True)
            
            with open(report_file_path,"w") as report_file:
                json.dump(report,report_file,indent=6)

            logging.info(f"Report has been created Successfuly and report name is : {report}")

            return report

        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def save_data_drift_report_page(self):
        try:
            dashboard =Dashboard(tabs=[DataDriftTab()])
            train_df,test_df = self.get_train_df_and_test_df()
            dashboard.calculate(train_df,test_df)
            report_page_file_path = self.data_validation_config.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir,exist_ok=True)
            dashboard.save(report_page_file_path)

        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def is_data_drift_found(self):
        try:
            
            get_and_saved_data_drift_report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()

            return True
        except Exception as e:
            raise ExceptionHendler(e,sys) from e

    def initiate_data_validation(self):
        try:
            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path, 
                report_file_path = self.data_validation_config.report_file_path, 
                report_page_file_path = self.data_validation_config.report_page_file_path, 
                is_validated = True, 
                message="Data validation Performed Successfuly"
            )

            return data_validation_artifact
        except Exception as e:
            raise ExceptionHendler(e,sys) from e