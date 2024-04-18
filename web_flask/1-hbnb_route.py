#!/usr/bin/python3

from flask import Flask
"""
Script that starts a Flask web application:
- Routes:
  - /: display “Hello HBNB!”
  - /hbnb: display “HBNB”
"""

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Displays Hello HBNB"""
    return 'Hello HBNB!'


@app.route("/hbnb")
def hbnb():
    """Displays HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
