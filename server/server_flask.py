#!/bin/env python3
import os
from flask import Flask, render_template

template_dir = ''

app = Flask(__name__, template_folder=template_dir, static_url_path='', static_folder=template_dir)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/health/readiness')
def readiness():
    # return("Hello world")
    resp = app.response_class(response='Ready', status=200, mimetype='text/text')
    return(resp)

@app.route('/about')
def about():
    return("Hello world")


if __name__ == "__main__":
    template_dir = os.getcwd()
    print('Main' + template_dir)
    app.run(host='localhost', port=8080, debug=True)
else:
    template_dir = os.getcwd() + '/server'
    print(template_dir)