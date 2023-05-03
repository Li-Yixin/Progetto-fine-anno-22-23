# save this as hello.py
from flask import Flask


app = Flask(__name__)


@app.route("/units")
def hello():
    return "Solar system"