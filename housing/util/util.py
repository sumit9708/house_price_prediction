from distutils.command.config import config
import os,sys
from tkinter import E
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from housing.logger import logging
from housing.exception import ExceptionHendler
import yaml
from housing.constant import *
import pandas as pd
import numpy as np
import dill



def write_yaml_file(file_path:str,data:dict=None):
    """
    Create yaml file 
    file_path: str
    data: dict
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path,"w") as yaml_file:
            if data is not None:
                yaml.dump(data,yaml_file)
    except Exception as e:
        raise ExceptionHendler(e,sys) from e

def read_yaml_file(file_path:str):


    """
    This function will read data inside the config.yaml file and will return by slicing
    """

    try:
        
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise ExceptionHendler(e,sys) from e

def save_numpy_array_data(file_path:str,array:np.array):
    try:

        """
         Save numpy array data to file
         file_path: str location of file to save
         array: np.array data to save
        """

        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as array_file:
            np.save(array_file,array)


    except Exception as e:
        raise ExceptionHendler(e,sys) from e

def load_numpy_array_data(file_path:str)->np.array:
    try:

        """
        load numpy array data from file
        file_path: str location of file to load
        return: np.array data loaded
        """
        with open(file_path,"rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise ExceptionHendler(e,sys) from e

def save_preprocessing_object(file_path:str,obj):
    try:

        """
        This function will save object to the give file path

        file_path : str

        obj is any object
        """

        obj_dir = os.path.dirname(file_path)
        os.makedirs(obj_dir,exist_ok=True)

        with open(file_path,"wb") as object_file:
            dill.dump(obj,object_file)

    except Exception as e:
        raise ExceptionHendler(e,sys) from e

def load_preprocessing_object(file_path:str):
    try:

        """
        file_path : str
        """
        with open(file_path,"rb") as obj_file:
            return dill.load(obj_file)
    except Exception as e:
        raise ExceptionHendler(e,sys) from e

def load_data(file_path: str, schema_file_path: str) -> pd.DataFrame:
    try:
        datatset_schema = read_yaml_file(schema_file_path)

        schema = datatset_schema[DATASET_SCHEMA_COLUMNS_KEY]

        dataframe = pd.read_csv(file_path)

        error_messgae = ""


        for column in dataframe.columns:
            if column in list(schema.keys()):
                dataframe[column].astype(schema[column])
            else:
                error_messgae = f"{error_messgae} \nColumn: [{column}] is not in the schema."
        if len(error_messgae) > 0:
            raise Exception(error_messgae)
        return dataframe

    except Exception as e:
        raise ExceptionHendler(e,sys) from e
    
