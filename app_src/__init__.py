from flask import Flask
from .config import Config

hcc_app = Flask(__name__)
hcc_app.config.from_object(Config)