from setuptools import setup,find_packages
from typing import List

### here we are giving all the details of the project to setup.

PROJECT_NAME = "house_price_prediction"
AUTHOR = "Sumit Bhagat"
VERSION = "0.0.3"
DESCRIPTION = "This is machine learning project for house price prediction in bangalore location"
#PACKAGES = ["housing"]
REQUIRED_FILES = "requirements.txt"
DATA = "-e ."

def get_required_files()->List[str]:

    """
    Descriptiob :- This function going to return list of all the libarary inside the requirements.txt file.
    """
    with open(REQUIRED_FILES) as requirements_file:
        
        requirement_list = [requirement.replace("\n","")  for requirement in requirements_file.readlines()]
        if DATA in requirement_list:
            requirement_list.remove(DATA)
        return requirement_list

setup(

name = PROJECT_NAME,
author=AUTHOR,
version=VERSION,
description=DESCRIPTION,
packages=find_packages(),
install_requires= get_required_files()

)
