import requests
import json
import re

def cleanhtml(raw_html):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw_html)
	return cleantext

def navigate(start, end):
	start = start.replace(" ", "+")
	end = end.replace(" ", "+")
	# To get your key, simply go to https://console.developers.google.com/apis/dashboard, enable the Directions API, create a API key and paste it below
	key="AIzaSyCS32VILSRfFUnvHCTULmgATk2XUuehbCg"
	urlToScrape = "https://maps.googleapis.com/maps/api/directions/json?origin="+start+"&destination="+end+"&key="+key

	response = requests.get(urlToScrape)

	text = response.text
	text = json.loads(text)

	if(text['status'] == "OK"):
		instructions = []
		i = 0
		for i, direction in enumerate(text['routes'][0]['legs'][0]['steps']):
			direction = cleanhtml(direction['html_instructions']).replace("Restricted usage road", "")
			if(i == 0):
				instructions.append("First, " + direction)
			elif("Destination will be on" in direction):
				instructions.append("The destination will be on " + direction.split("Destination will be on ")[1])
			else:
				if(direction not in instructions):
					instructions.append("Next, " + direction)
		instructions.insert(0, i+1)
		return(instructions)
	else:
		return("An error occured")

def timeToPlace(start, end):
	start = start.replace(" ", "+")
	end = end.replace(" ", "+")
	urlToScrape = "https://maps.googleapis.com/maps/api/directions/json?origin="+start+"&destination="+end+"&key=AIzaSyCS32VILSRfFUnvHCTULmgATk2XUuehbCg"

	response = requests.get(urlToScrape)

	text = response.text
	text = json.loads(text)
	if(text['status'] == "OK"):
		return("It will take " + text['routes'][0]['legs'][0]['duration']['text'].replace("mins", "minutes"))
	else:
		return("An error occured")