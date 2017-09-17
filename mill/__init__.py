from flask import Flask

mill = Flask(__name__)
mill.config.from_object('config')

from . import views

