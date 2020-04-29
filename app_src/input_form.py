from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class InputForm(FlaskForm):
    afp = FloatField("AFP Value", validators=[InputRequired(message="This field is required"),NumberRange(min=0.0, max=10000.0,message="Value not valid. Must be in range [0,10000]")])
    afp_l3 = FloatField("AFP-L3 Value", validators=[InputRequired(message="This field is required"),NumberRange(min=0.0, max=10000.0,message="Value not valid. Must be in range [0,10000]")])
    dcp = FloatField("DCP Value", validators=[InputRequired(message="This field is required"),NumberRange(min=0.0, max=10000.0,message="Value not valid. Must be in range [0,10000]")])
    submit = SubmitField("Predict")