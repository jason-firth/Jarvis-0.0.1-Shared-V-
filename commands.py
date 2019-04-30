from gtts import gTTS
import speech_recognition as sr
import os
import pipes
import sys
import subprocess
import re
# import webbrowser
import smtplib
import urllib
import urllib.request
import pygame
# from geopy.geocoders import Nominatim
# from weather import Weather
from random import randint
import pyttsx3
import socket
import vlc
# import forecastio
import json
# from voiceit2 import VoiceIt2
from time import gmtime, strftime
import pyaudio
import random
import wave
import requests
# import hud.py
# import geocoder
import serial
from bluetooth import *
from datetime import datetime

# Directions
from directions import navigate
from directions import timeToPlace
direc = []
stepNum = 0

# Weather
from weather import getTemperature
from weather import getPressure
from weather import getHumidity

contacts = {
	"aaron":"###-###-####",
	"mom": "###-###-####",
	"dad": "###-###-####",
	"sister": "###-###-####",
	"dan": "###-###-####"
}

'''
With commands, if you don't want Jarvis to reply, make sure you still return "command no voice".
If you want Jarvis to say something, return "(What you want jarvis to say)"

'''

def internet_on():
	for timeout in [1,5,10,15]:
		try:
			print ("checking internet connection..")
			socket.setdefaulttimeout(timeout)
			host = socket.gethostbyname("www.google.com")
			s = socket.create_connection((host, 80), 2)
			s.close()
			return True

		except Exception:
			return False


def messagePerson(number, message):
	# MAC Address
	addr = "50:55:27:8C:E1:06"

	# search for theadr
	uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
	service_matches = find_service( uuid = uuid, address = addr )

	if len(service_matches) == 0:
		return("Sorry Sir, Your device wasn't found")

	first_match = service_matches[0]
	port = first_match["port"]
	name = first_match["name"]
	host = first_match["host"]


	# Create the client socket
	sock=BluetoothSocket( RFCOMM )
	sock.connect((host, port))

	# print("connected. Type stuff")
	# print((number+"|"+message).replace("-", "").replace("406",""))
			
	sock.send(number+"|"+message.replace("406",""))
	sock.close()


def checkCommand(command, ser, moviePlaying, player, paused, serverStarted, usingArduino, usingMedia):
	global direc, stepNum
	if 'joke' in command and internet_on():
		res = requests.get(
				'https://icanhazdadjoke.com/',
				headers={"Accept":"application/json"}
				)
		if res.status_code == requests.codes.ok:
			return(str(res.json()['joke']))
			engine.say(str(res.json()['joke']))
			engine.runAndWait()
		else:
			return('oops! I ran out of jokes')

	# Weather
	elif 'weather in' in command and internet_on():
		city = command.split("weather in ")[1]
		return("The temperature in " + city + " is " + getTemperature(city) + " degrees fahrenheit. The pressure is " + getPressure(city) + ". The humidity is " + getHumidity(city) + ".")
	elif 'temp in' in command and internet_on():
		city = command.split("temp in ")[1]
		return("The temperature in " + city + " is " + getTemperature(city) + ".")
	elif 'temperature in' in command and internet_on():
		city = command.split("temperature in ")[1]
		return("The temperature in " + city + " is " + getTemperature(city) + ".")
	elif 'pressure in' in command and internet_on():
		city = command.split("pressure in")[1]
		return("The pressure is " + getPressure(city) + ".")
	elif 'humidity in' in command and internet_on():
		city = command.split("humidity in")[1]
		return("The humidity is " + getHumidity(city) + ".")
		
	elif 'time' in command:
		now = datetime.now()
		return("It is " + now.strftime('%I:%M %p'))

	#get date
	elif 'date' in command:
		month = "";
		now=datetime.now()
		if(strftime("%m") == "01"):
			month = "January"
		elif(strftime("%m") == "02"):
			month = "Febuary"
		elif(strftime("%m") == "03"):
			month = "March"
		elif(strftime("%m") == "04"):
			month = "April"
		elif(strftime("%m") == "05"):
			month = "May"
		elif(strftime("%m")== "06"):
			month = "June"
		elif(strftime("%m") == "07"):
			month = "July"
		elif(strftime("%m") == "08"):
			month = "August"
		elif(strftime("%m") == "09"):
			month = "September"
		elif(strftime("%m") == "10"):
			month = "October"
		elif(strftime("%m") == "11"):
			month = "November"
		else:
			month = "December"
		if(strftime("%d")=="1"):
			return("The date is "+ month + " 1st, " + strftime("%Y"))
		elif(strftime("%d")=="2"):
			return("The date is "+ month + " 2nd, " + strftime("%Y"))
		elif(strftime("%d")=="3"):
			return("The date is "+ month + " 3rd, " + strftime("%Y"))
		elif(strftime("%d")=="21"):
			return("The date is "+ month + " 21st, " + strftime("%Y"))
		elif(strftime("%d")=="22"):
			return("The date is "+ month + " 22nd, " + strftime("%Y"))
		elif(strftime("%d")=="23"):
			return("The date is "+ month + " 23rd, " + strftime("%Y"))
		else:
			return("The date is " + month + strftime("%d") + ", " + strftime("%Y"))
	elif 'what\'s up' in command:
		return('Just doing my thing')
	elif 'help' in command:
		return('I can inform you of the time, tell you the date, and play entertainment for you')
	elif 'play' in command and usingMedia:
		movieInput = command.split("play")[1].replace(" ", "")

		# If you plan on using music, run the command ls /media/pi/ and replace 8891-D645/ with whatever pops up. Make sure to include the /
		directory = "/media/pi/8891-D645/"
		movies = {}
		moviesList = []

		# If you have any other filetpyes, add them here
		filetypes = ["mp4","mp3", "m4v", "m4a"]
		
		for movie in os.listdir(directory):
			if("." in movie):
				if(movie.split(".")[1] in filetypes):
					pathToMovie = directory+movie
					movies[movie.split(".")[0]] = pathToMovie
					moviesList.append(movie.split(".")[0].replace("_", " ").replace(" ", ""))

					print("Movie: " + movie.split(".")[0] + " Location: " + pathToMovie)

		print(movies)
		# FOR JARVIS: change movieToPlay to command.split("play")[1]
		movieToPlay = movieInput
		if(movieToPlay in moviesList):
			# os.system("vlc " + movies[movieToPlay] + " --fullscreen --play-and-exit")
			player = vlc.MediaPlayer(movies[movieToPlay])

			player.set_fullscreen(True)
			player.video_set_mouse_input(True)
			player.video_set_key_input(True)
			os.system("")
			player.play()
			moviePlaying = True
			return("command no voice")
		else:
			return("That does not exist")
	elif 'pause' in command and usingMedia:
		if(not paused and moviePlaying):
			player.pause()
			paused = True
			return("command no voice")
		else:
			return("Nothing is playing")
	elif 'quit' in command and usingMedia:
		if(moviePlaying):
			player.stop()
			moviePlaying = False
			return("command no voice")
		else:
			return("Nothing is playing")
	elif 'resume' in command and usingMedia:
		if(moviePlaying and paused):
			player.play()
			paused = False
			moviePlaying = True
			return("command no voice")
	elif 'volume to' in command:
		setToPercent = command.split("volume to")[1]
		os.system("amixer set 'PCM' " + setToPercent+"%")
		return("command no voice")
	elif 'go to the middle' in command and usingMedia:
		if(moviePlaying):
			player.set_position(0.5)
			return("command no voice")
		else:
			return("Nothing is playing")
	elif 'go to the start' in command or 'go the beginning' in command and usingMedia:
		if(moviePlaying):
			player.set_position(0.2)
			return("command no voice")
		else:
			return("Nothing is playing")
	elif 'go to the end' in command and usingMedia:
		if(moviePlaying):
			player.set_position(0.9)
			return("command no voice")
		else:
			return("Nothing is playing")
	elif 'go to' in command and usingMedia:
		if(moviePlaying):
			position = command.split("go to ")[1]
			player.set_position((int(position)/100))
			return("command no voice")
		else:
			return("Nothing is playing")
	elif 'flip a coin' in command:
		randomNum = random.randint(0,1)
		if(randomNum == 0):
			return("It was heads")
		else:
			return("It was tails")
	elif 'color to' in command and usingArduino:
		color = command.split("color to")[1]
		ser.write(color.encode())
		return("Changing Color")
	elif 'message' in command and serverStarted:
			foundCon = False
			personLength = 0
			temp = command.split("message ")[1]
			for person in contacts:
				if(person in temp):
					foundCon = True
					number = contacts[person]
					personLength = len(person)
			if(not foundCon):
				number = temp[:12].replace("-", "")
				message = temp[12:]
			else:
				message = temp[personLength:]
			print(number, message)
			messagePerson(number, message)
			return("command no voice")
	elif 'how long will it take to get to' in command and internet_on():
		start = command.split("how long will it take to get to")[1]
		start = start.split("from")[0]
		end = command.split("from")[1]
		return(timeToPlace(start, end))
	elif 'how long will it take to go to' in command and internet_on():
		start = command.split("how long will it take to go to")[1]
		start = end.split("from")[0]
		end = command.split("from")[1]
		return(timeToPlace(start, end))
	elif 'navigate to' in command and "from " in command and internet_on():
		end1 = command.split("to ")[1]
		end2 = end1.split("from ")[1]
		start = end1.split("from ")[0]
		if(navigate(start, end2) != "An error occured"):
			for thing in navigate(start, end2):
				direc.append(thing)
		stepNum = 1
		return("Navigating to " + start + " From " + end2 + ". There are " + str(direc[0]) + " steps. " + direc[1])
	elif 'take me to' in command and "from " in command and internet_on():
		end1 = command.split("take me to ")[1]
		end2 = end1.split("from ")[1]
		start = end1.split("from ")[0]
		if(navigate(start, end2) != "An error occured"):
			for thing in navigate(start, end2):
				direc.append(thing)
		stepNum = 1
		return("Navigating to " + start + " From " + end2 + ". There are " + str(direc[0]) + " steps. " + direc[1])
	elif 'next direction' in command or 'next step' in command and internet_on():
		if(stepNum != 0 and not ((stepNum+1) > len(direc))):
			stepNum += 1
			if(stepNum+1 == len(direc)):
				stepNum = 0
				direc = []
			return(direc[stepNum])
		else:
			return("You haven't started navigation")
	elif 'previous direction' in command or 'last direction' in command or 'last step' in command or 'previous step' in command and internet_on():
		if(stepNum != 0 or stepNum != 1):
			stepNum -= 1
			return(direc[stepNum])
		else:
			return("You haven't started navigation")
	elif 'exit navi' in command or 'stop navi' in command:
		stepNum = 0
		direc = []
		return("Exiting Route")

	else:
		return("Please repeat that")
	# assistant(myCommand())
	# elif 'start hud' in command:
	# 	starthud()
	# elif 'stop hud' in command:
	# 	stophud()

	
	# elif 'stop hud' in command:
	# 	stophud()
	# elif 'start hud' in command:
	# 	os.system("python3 hud.py")

