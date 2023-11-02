#!/usr/bin/env python3

"""
0.Basic flask app
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=["GET"], strict_slash=False)
def greeting():
        """
    a route is created with a get method
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
