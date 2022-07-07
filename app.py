from distutils.debug import DEBUG
from flask import Flask
from housing.logger import logging
from housing.exception import ExceptionHendler
import os,sys

app = Flask(__name__)

@app.route("/test",methods = ['POST','GET'])

def test():
    try:
        raise Exception("This is self generated Exception")
        #logging.info("This is the testing for my logger file")
        #return "This is a testing file for ML project"
    except Exception as e:
        housig_exception = ExceptionHendler(e,sys)
        logging.info(housig_exception.error_message)
        logging.info("This is testion for logs")

    return "This is a testing file for ML project"


if __name__=="__main__":
    app.run(debug=True)