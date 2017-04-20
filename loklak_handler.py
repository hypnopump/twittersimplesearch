#-*- coding: utf-8 -*-
# Code written by Eric Alcaide - https://github.com/EricAlcaide

import sys
import requests
import json

# Gets the data from loklak API
def getData(query):
	request = requests.get('http://loklak.org/api/search.json?q='+query).json()
	return request

# Prints the interesting data on screen
def organizeData(unformated):
	temp= [] # Simpler way to define a list
	tweets = unformated['statuses']

	for ind in tweets:
		link = ind['link']
		username = ind['screen_name']
		name = ind['user']['name']
		text = ind['text']

		dict1 = {'link':link,'username':username,'name':name,'text':text}
		temp.append(dict1)

	return temp

def serveData(query):
	unformated = getData(query)
	organized = organizeData(unformated)

	return organized