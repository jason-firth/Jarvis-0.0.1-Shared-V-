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

def checkCommand(command, moviePlaying, player, paused, usingBluetooth, bluetoothNotWanted, serverStarted):
    if 'time' in command:
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
    #elif 'joke' in command:
        #res = requests.get(
        #		'https://icanhazdadjoke.com/',
        #		headers={"Accept":"application/json"}
        #		)
        #if res.status_code == requests.codes.ok:
            #return(str(res.json()['joke']))
            #engine.say(str(res.json()['joke']))
            #engine.runAndWait()
        #else:
            #return('oops! I ran out of jokes')

    # elif ' in' in command:
    #     reg_ex = re.search('weather in (.*)', command)
    #     if reg_ex:
    #         city = reg_ex.group(1)
    #         weather = Weather()
    #         location = geolocator.geocode(city)
    #         placeweather = location.latitude, location.longitude
    #         #Get weather
    #         observation = owm.weather_at_place(city)
    #         w = observation.get_weather()
    #         currentTemperature = w.get_temperature('celsius')
    #         tempCelsius = int(currentTemperature['temp']) * 1.8
    #         tempFahrenheit = tempCelsius + 32
    #         tempFahrenheit = str(tempFahrenheit)
    #         return("It is "+tempFahrenheit + " degrees Fahrenheit")
    #         print ("It is "+tempFahrenheit + " degrees Fahrenheit")

    #elif 'lockdown in command:

    elif 'dandy\'s favorite' in command:
        return('Dandy\'s favorite student is Jason. He also likes Aaron equally as much.')

    elif 'play' in command:
        movieInput = command.split("play")[1].replace(" ", "")
        directory = "/media/pi/8891-D645/"
        movies = {}
        moviesList = []
        filetypes = ["mp4","mp3", "m4v"]
        
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

        else:
            return("That does not exist")
    elif 'pause' in command:
        if(not paused and moviePlaying):
            player.pause()
            paused = True
        else:
            return("Nothing is playing")
    elif 'quit' in command:
        if(moviePlaying):
            player.stop()
            moviePlaying = False
        else:
            return("Nothing is playing")
    elif 'resume' in command:
        if(moviePlaying and paused):
            player.play()
            paused = False
            moviePlaying = True
    elif 'volume to' in command:
        setToPercent = command.split("volume to")[1]
        os.system("amixer set 'PCM' " + setToPercent+"%")
    elif 'go to the middle' in command:
        if(moviePlaying):
            player.set_position(0.5)
        else:
            return("Nothing is playing")
    elif 'go to the start' in command or 'go the beginning' in command:
        if(moviePlaying):
            player.set_position(0.2)
        else:
            return("Nothing is playing")
    elif 'go to the end' in command:
        if(moviePlaying):
            player.set_position(0.9)
        else:
            return("Nothing is playing")
    elif 'go to' in command:
        if(moviePlaying):
            position = command.split("go to ")[1]
            player.set_position((int(position)/100))
        else:
            return("Nothing is playing")
    elif 'color to' in command:
        color = command.split("color to")[1]
        ser.write(color.encode())
    elif 'enable app' in command or 'start app' in command or 'initialize app' in command:
        # os.system("sudo python3 ~/Jarvis-0.0.1-Shared-V-/blu.py")
        return('Starting app compatability')
        serverStarted = True
        bluetoothNotWanted = False
        # assistant(myCommand())
    # elif 'start hud' in command:
    # 	starthud()
    # elif 'stop hud' in command:
    # 	stophud()

    
    # elif 'stop hud' in command:
    # 	stophud()
    # elif 'start hud' in command:
    # 	os.system("python3 hud.py")
    else:
        return('I don\'t know what you mean!')