import requests
import time

crontable = []
outputs = []

def process_message(data):
	isbot = '<@U04F3NB5M>'
	print data

	# send a direct message to isbot with a command
	if data['text'] and isbot in data['text']:
		if 'tableflip' in data['text']:
			tableflip = requests.get('http://tableflipper.com/json')
			tableflip = tableflip.json()
			print tableflip
			outputs.append([data['channel'], tableflip['gif']])
		else:
			outputs.append([data['channel'], "Sorry, I do not understand"])
			outputs.append([data['channel'], "Commands I know: tableflip"])

	if data['text'] == isbot:
		print 'someone said just isbot'
		outputs.append([data['channel'], "Commands I know: tableflip"])
