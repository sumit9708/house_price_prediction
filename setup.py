from setuptools import setup,find_packages
from typing import List

### here we are giving all the details of the project to setup.

PROJECT_NAME = "house_price_prediction"
AUTHOR = "Sumit Bhagat"
VERSION = "0.0.2"
DESCRIPTION = "This is machine learning project for house price prediction in bangalore location"
#PACKAGES = find_packages() #["housing"],
REQUIRED_FILES = "requirements.txt"

def get_required_files()->List[str]:

    """
    Descriptiob :- This function going to return list of all the libarary inside the requirements.txt file.
    """
    with open(REQUIRED_FILES) as requirements_file:
        return requirements_file.readlines()

setup(

name = PROJECT_NAME,
author=AUTHOR,
version=VERSION,
description=DESCRIPTION,
packages=find_packages(),
install_requires= get_required_files()

)

if __name__=="__main__":
    print(get_required_files())
