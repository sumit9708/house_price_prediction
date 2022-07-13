import os,sys
from tkinter import E
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from housing.logger import logging
from housing.exception import ExceptionHendler
import yaml
from housing.constant import *


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

    
