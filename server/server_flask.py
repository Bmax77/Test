#!/bin/env python3
import os
from flask import Flask, render_template, request

template_dir = ''

app = Flask(__name__, template_folder=template_dir, static_url_path='', static_folder=template_dir)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/stop')
def stop():
    shutdown_func = request.environ.get('werkzeug.server.shutdown')
    if shutdown_func is None:
        raise RuntimeError('Not running werkzeug')
    shutdown_func()
    return "Shutting down..."


@app.route('/health/readiness')
def readiness():
    # return("Hello world")
    resp = app.response_class(response='Ready', status=200, mimetype='text/text')
    return(resp)

@app.route('/about')
def about():
    return("Hello world")

@app.route('/cards/<card_number>', methods=['GET'])
def card(card_number):
    card_number = card_number[:6]
    print(card_number)
    with open('server/binlist-data.csv') as f:
        if card_number in f.read():
            return('{"Bank":' + str(card_number)+ '}')
        else:
            return('{"Bank":"hot found"}')



if __name__ == "__main__":
    template_dir = os.getcwd()
    print('Main' + template_dir)
    app.run(host='localhost', port=8080, threaded=True, debug=True)
else:
    template_dir = os.getcwd() + '/server'
    print(template_dir)