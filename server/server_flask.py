#!/bin/env python3
import os
from flask import Flask, render_template, request
import pathlib
import re
import csv
import json
import sys

# template_dir = ''
data = ()

app = Flask(__name__, template_folder='', static_url_path='', static_folder='')

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
    resp = app.response_class(response='Ready', status=200, mimetype='text/text')
    return(resp)

@app.route('/cards/<card_number>', methods=['GET'])
def card(card_number):
    card_number = re.match(r'\d{16,20}', card_number)
    if card_number is not None:
        resp = None
        card_number = card_number.group(0)
        for row in data:
            if  row[0] in card_number[:len(row[0])]:
                print(row)
                resp = app.response_class(response=json.dumps(row), status=200, mimetype='text/text')
                break
            else:
                resp = app.response_class(response='Not found', status=404, mimetype='text/text')
        return(resp)
    else:
        resp = app.response_class(response='Internal server error', status=500, mimetype='text/text')
        return(resp)




if __name__ == "__main__":
    port = 8080
    if len(sys.argv) == 3 and '-p' in sys.argv: 
        port = sys.argv[2]        
    path = pathlib.Path(__file__).parent.resolve()
    with open(path.joinpath('binlist-data.csv'), newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    app.run(host='0.0.0.0', port=port, threaded=True, debug=False)
