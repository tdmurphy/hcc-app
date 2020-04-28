from flask import Flask, render_template, flash

from . import hcc_app
from .input_form import InputForm


@hcc_app.route("/")
def home():
    return render_template("home.html")

@hcc_app.route("/predict", methods=['GET','POST'])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        flash("Prediction requested for AFP: {}, AFP-L3: {}, DCP: {}".format(form.afp.data, form.afp_l3.data, form.dcp.data))
    return render_template("predict.html", form=form)
