from flask import Flask

hcc_app = Flask(__name__)

@hcc_app.route("/")
def home():
    return "Hello World"