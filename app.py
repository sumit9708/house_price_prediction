from distutils.debug import DEBUG
from flask import Flask

app = Flask(__name__)

@app.route("/test",methods = ['POST','GET'])

def test():
    return "This is a testing file for ML project"

if __name__=="__main__":
    app.run(debug=True)