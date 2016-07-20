"""
The flask application package.
"""

# import logging
# from logging.handlers import FileHandler

from flask import Flask
app = Flask(__name__)

app.debug = True

# handler = FileHandler('D:\home\site\wwwroot\app.log')
# handler.setLevel(logging.DEBUG)
# app.logger.addHandler(handler)

import FlaskWebProject.views
