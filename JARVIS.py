from gtts import gTTS
import speech_recognition as sr
import os
import pipes
import sys
import subprocess
import re
# import webbrowser
import smtplib
import urllib.request
import pygame
# from geopy.geocoders import Nominatim
# from weather import Weather
from random import randint
import pyttsx3
import vlc
# import forecastio
import json
# from voiceit2 import VoiceIt2
from time import gmtime, strftime
import pyaudio
import wave
import requests
# import hud.py
# import geocoder
import serial
from bluetooth import *
from datetime import datetime

moviePlaying = False

player = ""

ser = serial.Serial('/dev/ttyACM0', 9600)
ser.write("255,0,0".encode())
ser.write("0,255,0".encode())
ser.write("0,0,255".encode())
from commands import checkCommand
serverStarted = False
# Used to mute jarvis
#os.system("amixer set 'PCM' 0%")
usingBluetooth = False
engine = pyttsx3.init()
loopCommand = True
now = datetime.now()
AmPm=now.strftime('%p')
paused = False
if(AmPm =='PM'):
	engine.say('Good evening sir, we are online and ready.')
	engine.runAndWait()
else:
	engine.say('Good morning sir, we are online and ready.')
	engine.runAndWait()

#engine.say('Please authenticate')
#engine.runAndWait()

#User authentication
# def authStart():
#         FORMAT = pyaudio.paInt16
#         CHANNELS = 2
#         RATE = 44100
#         CHUNK = 1024
#         RECORD_SECONDS = 9
#         WAVE_OUTPUT_FILENAME = "auth2.wav"
		 
#         audio = pyaudio.PyAudio()
		 
#         # start Recording
#         stream = audio.open(format=FORMAT, channels=CHANNELS,
#                         rate=RATE, input=True,
#                         frames_per_buffer=CHUNK)
#         print ("recording...")
#         frames = []
		 
#         for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#             data = stream.read(CHUNK)
#             frames.append(data)
#         print ("finished recording")
		 
		 
#         # stop Recording
#         stream.stop_stream()
#         stream.close()
#         audio.terminate()
		 
#         waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
#         waveFile.setnchannels(CHANNELS)
#         waveFile.setsampwidth(audio.get_sample_size(FORMAT))
#         waveFile.setframerate(RATE)
#         waveFile.writeframes(b''.join(frames))
#         waveFile.close()
#         responseAuth=my_voiceit.voice_verification("usr_b9c994a6bc4149968eab59c6c9ca085b", "en-US", "hey jarvis you up initiate boot sequence two user stark", "auth2.wav")
#         print(responseAuth)
#         if("Successfully verified" in responseAuth["message"]):
#             authenticated = True
#         else:
#             engine.say('try again')
#             engine.runAndWait()
#             authStart()

# authStart()
connected = False
bluetoothNotWanted = True
# os.system("sudo python3 /home/pi/Jarvis-0.0.1-Shared-V-/blu.py &")
os.system("mkfifo jarvis")
# geolocator = Nominatim(user_agent="JARVIS2")
def talkToMe(audio):
	"speaks audio passed as argument"
	engine.say(audio)
	engine.runAndWait()
	print(audio)
	#for line in audio.splitlines():
	#	os.system("say " + audio)

	#  use the system's inbuilt say command instead of mpg123
	#  text_to_speech = gTTS(text=audio, lang='en')
	#  text_to_speech.save('audio.mp3')
	#  os.system('mpg123 audio.mp3')


def myCommand():
	global usingBluetooth, bluetoothNotWanted, connected, serverStarted
	"listens for commands"
	#if(not verified):
	#   authStart()
	if(not usingBluetooth):

		r = sr.Recognizer()
		
		with sr.Microphone() as source:
			print('Yes Sir?')
			r.pause_threshold = 0.5
			r.non_speaking_threshold = 0.3
			r.adjust_for_ambient_noise(source, duration=1)
			audio = r.listen(source)
		try:
			command = r.recognize_google(audio).lower()
			print('You said: ' + command + '\n')
		except sr.UnknownValueError:
			print('Your last command couldn\'t be heard')
			command = myCommand();
		# Below is used for keyboard input
		# command = input ("command: ")
		print(command)
		usingBluetooth = False
	else:
		command = ""
		# server_sock=BluetoothSocket( RFCOMM )
		# server_sock.bind(("",PORT_ANY))
		# server_sock.listen(1)

		# port = server_sock.getsockname()[1]

		# uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"


		# advertise_service( server_sock, "SampleServer", service_id = uuid, service_classes = [ uuid, SERIAL_PORT_CLASS ], profiles = [ SERIAL_PORT_PROFILE ])

		# client_sock, client_info = server_sock.accept()
		# print("Accepted connection from ", client_info)
		print("BLUETOOTH")
		# server_sock=BluetoothSocket( RFCOMM )
		# server_sock.bind(("",PORT_ANY))
		# server_sock.listen(1)
		# port = server_sock.getsockname()[1]
		# uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
		# client_sock, client_info = server_sock.accept()
		try:
			data = client_sock.recv(1024)
			command = data.decode('utf-8')
			if("USER:DISCONNECT" in command):
				connected = False
				bluetoothNotWanted = True
				serverStarted = False
				usingBluetooth = False
			print(command)
		except IOError:
			pass

		# print("disconnected")

		# client_sock.close()
		# server_sock.close()
		# print("all done")
		# command = subprocess.check_output(["eval $(cat bluetooth)"])
		# command = os.popen("eval $(cat bluetooth)").read()
		# t = pipes.Template()
		# f = t.open('bluetooth', 'r')
		# print(f.read().strip())
		# command = str(f.read().strip())
		# usingBluetooth = True
	return command


# def alarmjarvis(endTime, ampm):
#     alarmGoing = True
#     print("confirm set alarm for " + endTime)
#     while True:
#         assistant(myCommand())
#         now = datetime.now()
#         if((now.strftime('%I:%M') + ampm) == endTime):
#             if(alarmGoing == True):
#                 if(ampm == "a.m."):
#                     engine.say('Good morning sir, this is you alarm for ' + now.strftime('%I:%M') + ampm)
#                     engine.runAndWait()
#                     alarmGoing = False
#                 else:
#                     engine.say('Good afternoon sir, this is you alarm for ' + now.strftime('%I:%M') + ampm)
#                     engine.runAndWait()
#                     alarmGoing = False


def assistant(command):
	global moviePlaying, player, paused, usingBluetooth, bluetoothNotWanted, serverStarted
	"if statements for executing commands"
	if 'jarvis ' in command:
		if 'enable app' in command or 'start app' in command or 'initialize app' in command:
			# os.system("sudo python3 ~/Jarvis-0.0.1-Shared-V-/blu.py")
			talkToMe('Starting app')
			serverStarted = True
			bluetoothNotWanted = False
		else:
			
			if(checkCommand(command, ser, moviePlaying, player, paused, serverStarted) == "command no voice"):
				checkCommand(command, ser, moviePlaying, player, paused)
			else:
				talkToMe(checkCommand(command, ser, moviePlaying, player, paused, serverStarted))
	command = ""

#loop to continue executing multiple commands
while True:
	ser = serial.Serial('/dev/ttyACM0', 9600)
	server_sock=BluetoothSocket( RFCOMM )
	server_sock.bind(("",PORT_ANY))
	server_sock.listen(1)
	port = server_sock.getsockname()[1]
	uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
	#advertise_service( server_sock, "SampleServer", service_id = uuid, service_classes = [ uuid, SERIAL_PORT_CLASS ], profiles = [ SERIAL_PORT_PROFILE ])
	#client_sock, client_info = server_sock.accept()

#     if(authenticated):
	if(loopCommand):
		if(serverStarted and not bluetoothNotWanted):
			print("Server Ready!")
			ser = serial.Serial('/dev/ttyACM0', 9600)
			server_sock=BluetoothSocket( RFCOMM )
			server_sock.bind(("",PORT_ANY))
			server_sock.listen(1)
			port = server_sock.getsockname()[1]
			uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
			advertise_service( server_sock, "SampleServer", service_id = uuid, service_classes = [ uuid, SERIAL_PORT_CLASS ], profiles = [ SERIAL_PORT_PROFILE ])
			client_sock, client_info = server_sock.accept()
			print("Accepted connection from ", client_info)
			startedServer = True
			connected = True
			bluetoothNotWanted = False
			usingBluetooth = True
			while connected:
				assistant(myCommand())
		else:
			assistant(myCommand())

