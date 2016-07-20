"""
Routes and views for the flask application.
"""

import os

from datetime import datetime
from flask import render_template
from slugify import slugify
from FlaskWebProject import app
from FlaskWebProject import model

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home',
        upcoming=model.upcoming_workshops(),
        past=model.past_workshops(),
        slugify=slugify
    )


@app.route('/workshop/<title>')
def workshop(title):
    workshop = model.by_title(title)
    return render_template('workshop.html', title=title,
    workshop=workshop)


@app.route('/series/<name>')
def series(name):
    workshops = model.by_series(name)
    return render_template('series.html', title=name,
    series=name,
    workshops=workshops)

@app.route('/test')
def test():
    return str(os.environ)
