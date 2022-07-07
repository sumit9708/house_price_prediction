import os,sys
from housing.logger import logging
from housing.exception import ExceptionHendler

def demo_class():
    try:
        raise ExceptionHendler("This is self generated exception to test")
        logging.info("demo class has been created and logging and exception test started")
        return "Code is working Properly"
    except Exception as e:
        housing_exception = ExceptionHendler(e,sys)
        logging.info("This is a Demo to test")