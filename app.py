#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import os
import loklak_handler

app = Flask(__name__)

@app.route('/')
def web():
	return render_template('index.html')

@app.route('/search/', methods = ['GET', 'POST'])
def search():
	query = request.form['query']
	result = loklak_handler.serveData(query)
	if len(query) != 0:
		json_response = "../response/"+query+"/"
	else:
		json_response = "../no_response/"

	return render_template('result.html', list = result, json_response = json_response)

@app.route('/response/<query>/')
def JSONresponse(query):
	return jsonify(loklak_handler.serveData(query))

@app.route('/no_response/')
def JSONnull_response():
	return jsonify([{"Result": "No query specified, no results obtained"}])

if __name__ == '__main__':
	# Deploying
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
	# Debugging
	# app.run(debug=True, host='0.0.0.0')