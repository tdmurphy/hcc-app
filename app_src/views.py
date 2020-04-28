from flask import Flask, render_template

from . import hcc_app


@hcc_app.route("/")
def home():
    return render_template("home.html")

@hcc_app.route("/predict/")
def predict():
    return render_template("predict.html")
