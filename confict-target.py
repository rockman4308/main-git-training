from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell():
    <P>Hello world !!</P>
