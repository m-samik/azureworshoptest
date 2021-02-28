"""from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<center><h1>Hello !! its <b>Muhammad Sami</b></h1><br><img src='https://myimagestorage.blob.core.windows.net/mycontainerimages/mains.jpg' width=100px height=120px>" """
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('coming-soon.html')

if __name__ == '__main__':
    app.run(debug=True)
