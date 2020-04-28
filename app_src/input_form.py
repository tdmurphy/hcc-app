from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired, NumberRange

class InputForm(FlaskForm):
    afp = FloatField("AFP Value", validators=[InputRequired(message="This field is required"),NumberRange(min=-100.0, max=100.0,message="Value not valid. Must be in range [-100,100]")])
    afp_l3 = FloatField("AFP-L3 Value", validators=[InputRequired(message="This field is required"),NumberRange(min=-100.0, max=100.0,message="Value not valid. Must be in range [-100,100]")])
    dcp = FloatField("DCP Value", validators=[InputRequired(message="This field is required"),NumberRange(min=-100.0, max=100.0,message="Value not valid. Must be in range [-100,100]")])
    submit = SubmitField("Predict")