from distutils.debug import DEBUG
from flask import Flask
from housing.logger import logging

app = Flask(__name__)

@app.route("/test",methods = ['POST','GET'])

def test():
    logging.info("This is the testing for my logger file")
    return "This is a testing file for ML project"

if __name__=="__main__":
    app.run(debug=True)