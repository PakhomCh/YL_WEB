# from http.server import HTTPServer, CGIHTTPRequestHandler
# server_address = ("", 8000)
# httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
# httpd.serve_forever()

from flask import Flask
from flask import request
from flask import render_template
from flask import redirect


import cgi
import html

import generator


app = Flask(__name__)
app.config['SECRET_KEY'] = '0x000000'
user = '-1'


@app.route('/')
def inpage():
    return redirect('/home')

@app.route('/home')
def homepage():
    return render_template('home.html')


@app.route('/upgrade', methods=['POST', 'GET'])
def upgradepage():
    if request.method == 'GET':
        return render_template('upgrade.html')
    elif request.method == 'POST':
        print(request.form['param#1'])
        print(request.form['param#2'])
        print(request.form['param#3'])
        return result(request.form['param#1'], request.form['param#2'], request.form['param#3'])


@app.route('/info')
def infopage():
    return render_template('info.html')


@app.route('/result')
def result(val1, val2, val3):

    ans = generator.generate(int(val1), int(val2), int(val3))

    return render_template('result.html', SUG1=ans[0], SUG2=ans[1], SUG3=ans[2])


if __name__ == '__main__':
    app.run(port=8800, host='127.0.0.1')
