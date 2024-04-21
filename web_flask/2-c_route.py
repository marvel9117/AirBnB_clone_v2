#!/usr/bin/python3

from flask import Flask
from markupsafe import escape

"""
script that starts a Flask web application
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space )
"""

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """dispaly HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def cprint(text):
    """display C followed by the value of text"""
    return "C {}".format(escape(text.replace('_', ' ')))


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port='5000')
