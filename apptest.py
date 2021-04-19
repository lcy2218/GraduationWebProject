#!/usr/bin/env python
import json

from flask import Flask, flash, redirect, render_template, \
    request, url_for, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/test" , methods=['GET', 'POST'])
def test():
    global data1
    data = request.form.get('value')
    # data = json.loads(request.form.get('data'))
    if data:
        data1 = data
    data = data1
    print(data)
    # data = "累计确诊"
    # if data == "现有确诊":
    return jsonify({'value': data})

if __name__=='__main__':
    app.run(debug=True)