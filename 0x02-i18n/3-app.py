#!/usr/bin/env python3
""" Flask application """

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """ l18n Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    """ Gets the best matching language for the user """
    return request.accept_languages.best_match(Config.LANGUAGES)

@app.route("/")
def hello_world():
    """ Handle the default route """
    return render_template("3-index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
