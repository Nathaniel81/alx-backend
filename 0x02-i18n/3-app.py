#!/usr/bin/env python3
"""
Module: 3-app.py
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config(object):
    """Config class for configuring languages and timezons"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determines the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    """Handles the home route of the flask application"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
