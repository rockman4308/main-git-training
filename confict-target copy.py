from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world_again():
    return "<p>Hello!</p>"
