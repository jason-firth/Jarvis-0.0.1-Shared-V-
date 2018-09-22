from gtts import gTTS
import speech_recognition as sr
import os
import sys
import pyowm
import re
import webbrowser
import smtplib
import urllib.request
from geopy.geocoders import Nominatim
from datetime import date, timedelta
from weather import Weather
from random import randint
import pyttsx3
import forecastio
import json

owm = pyowm.OWM('fca9e4262edac35767e09e053c4c76d0')
engine = pyttsx3.init()
geolocator = Nominatim(user_agent="JARVIS2")
def talkToMe(audio):
    "speaks audio passed as argument"
    engine.say(audio)
    engine.runAndWait()
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Yes Sir?')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        engine.say('You said: ' + command)
        engine.runAndWait()
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        engine.say('Please repeat what you said.')
        engine.runAndWait()
        command = myCommand();


    return command


def assistant(command):
    "if statements for executing commands"

    if 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
            engine.say('Opening ' + url)
            engine.runAndWait()
        else:
            pass

    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')

    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
            engine.say(str(res.json()['joke']))
            engine.runAndWait()
        else:
            talkToMe('oops!I ran out of jokes')

    elif 'current weather in' in command:
        reg_ex = re.search('current weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = geolocator.geocode(city)
            placeweather = location.latitude, location.longitude
            #Get weather
            observation = owm.weather_at_place(city)
            w = observation.get_weather()
            currentTemperature = w.get_temperature('celsius')
            talkToMe(currentTemperature['temp'])
            print (currentTemperature['temp'])


    elif 'weather forecast in' in command:
        reg_ex = re.search('weather forecast in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            forecasts = location.forecast()
            for i in range(0,3):
                talkToMe('On %s will it %s. The maximum temperture will be %.1f degree.'
                         'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8))


    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'John' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message
            mail.sendmail('John Fisher', 'JARVIS2.0@protonmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')

        else:
            talkToMe('I don\'t know what you mean!')


talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
