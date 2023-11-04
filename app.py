from flask import Flask
from markupsafe import escape
#from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

#serve(app, port=8080)
#if __name__ == "__main__":
#    app.run(debug=True)
    #serve(app, host="127.0.0.1", port=8080)
