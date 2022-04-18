from flask import Flask, render_template
from config import Config
import requests
app = Flask(__name__)
app.config.from_object(Config)
from . import routes

