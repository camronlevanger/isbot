import requests
import time
from yelp import *

crontable = []
outputs = []

def process_message(data):
	isbot = '<@U04F3NB5M>'
	print data

	# send a direct message to isbot with a command
	if data.get('text') and isbot in data.get('text'):
		if 'tableflip' in data['text']:
			tableflip = requests.get('http://tableflipper.com/json')
			tableflip = tableflip.json()
			print tableflip
			outputs.append([data['channel'], tableflip['gif']])

		elif 'lunch' in data['text']:
			lunch = query_api('lunch', 'Provo, UT')
			print lunch
			outputs.append([data['channel'], "<@" + data['user'] + "> How about " + lunch['name'] + "? " + lunch['location']['address'][0] + " " + lunch['location']['city'] + " " + lunch['mobile_url']])
			outputs.append([data['channel'], "It has a " + str(lunch['rating']) + " star rating...here is what people are saying:"])
			outputs.append([data['channel'], lunch['reviews'][0]['excerpt']])
			outputs.append([data['channel'], lunch['image_url']])

		else:
			outputs.append([data['channel'], "Sorry, I do not understand"])
			outputs.append([data['channel'], "Commands I know: tableflip, lunch"])

	if data.get('text') and data.get('text') == isbot:
		print 'someone said just isbot'
		outputs.append([data['channel'], "Commands I know: tableflip, lunch"])
