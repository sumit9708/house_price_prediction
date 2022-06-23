from setuptools import setup
from typing import List

###Declearing Variables for the setup.py function.

PROJECT_NAME = "House Price Prediction"
AUTHOR = "Sumit Bhagat"
VERSION = "0.0.1"
DESCRIPTION = "This is the machine lerning project for house price prediction"
PACKAGES = ['housing']
INSTALL_REQUIRES = "requirements.txt"

def require_file_list()->List[str]:

    """
    Description - This function is going to return list of all the required module from 
    requirements.txt file and will provide to setup file.
    """

    with open(INSTALL_REQUIRES) as requirement_file:
        return requirement_file.readlines()

setup(

name = PROJECT_NAME,
author = AUTHOR,
version = VERSION,
packages =PACKAGES,
description=DESCRIPTION,
install_requires = require_file_list()
)

if __name__=="__main__":
    print(require_file_list())
