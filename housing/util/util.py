import os,sys
from tkinter import E
from housing.logger import logging
from housing.exception import ExceptionHendler
import yaml
from housing.constant import *

def read_yaml_file(file_path:str):


    """
    This function will read data inside the config.yaml file and will return by slicing
    """

    try:
        
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise ExceptionHendler(e,sys) from e

    