from flask import Flask, flash, render_template

from . import hcc_app
from .input_form import InputForm
from .lstm import LSTM

import torch

MODEL = LSTM(in_features=3, hidden_size=30, num_layers=1, out_features=2, drop_prob=0.2).to('cpu')
MODEL.load_state_dict(torch.load("models/pre_diagnosis_timepoint_strategy"))
MODEL.eval()

@hcc_app.route("/")
def home():
    return render_template("home.html")

@hcc_app.route("/predict", methods=['GET','POST'])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        flash("Prediction requested for AFP: {}, AFP-L3: {}, DCP: {}".format(form.afp.data, form.afp_l3.data, form.dcp.data))
        x = torch.tensor([form.afp.data, form.afp_l3.data, form.dcp.data])
        x = x.unsqueeze(0)
        x = x.unsqueeze(0)
        output = MODEL(x)
        output = output.squeeze(0)
        flash("RESULT: {}%% likelihood of HCC".format((output[0][0])*100))
    return render_template("predict.html", form=form)
