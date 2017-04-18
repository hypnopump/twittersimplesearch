#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import loklak_handler

app = Flask(__name__)

@app.route('/')
def web():
	return render_template('index.html')

@app.route('/search/', methods = ['GET', 'POST'])
def search():
	query = request.form['query']
	result = loklak_handler.serveData(query)
	json_response = "../response/"+query+"/"

	return render_template('result.html', list = result, json_response = json_response)

@app.route('/response/<query>/')
def JSONresponse(query):
	return jsonify(loklak_handler.serveData(query))

# @app.route('/test/')
# def test():
# 	username = "@eric_alcaide"
# 	user = "Eric"
# 	text = "This is a test lol"
# 	link = "https://github.com/EricAlcaide"
# 	return render_template('result.html', username = username, user = user, link = link, text = text)

if __name__ == '__main__':
    app.run()
