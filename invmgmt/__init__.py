from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '89ry2uqyr892n21vn32k4j'
from invmgmt import routes
    