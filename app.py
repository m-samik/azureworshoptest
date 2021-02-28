  
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<center><h1>Hello !! its <b> Muhammad Sami</b> </h1> </center>"
