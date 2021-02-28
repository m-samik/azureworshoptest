  
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<img src ="https://myimagestorage.blob.core.windows.net/mycontainerimages/mains.jpg">"
    return "<center><h1>Hello !! its <b> Muhammad Sami</b> </h1> </center>"
