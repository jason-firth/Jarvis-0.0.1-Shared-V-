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
from datetime import datetime
from weather import Weather
from random import randint
import pyttsx3
import forecastio
import json
from voiceit2 import VoiceIt2
from time import gmtime, strftime
import pyaudio
import wave
import alarm.py

engine = pyttsx3.init()

now = datetime.now()
Currenthour=now.strftime('%I')
AmPm=now.strftime('%p')

if(AmPm =='PM'):
    engine.say('Good evening sir, How can I help?')
    engine.runAndWait()
else:
    engine.say('Good morning sir, How can I help?')
    engine.runAndWait()




authenticated = False
my_voiceit = VoiceIt2('key_95dc2f49e21d462e9cc03c5a4ba7a076','tok_ff1b7e2e26db42f8b2ee9af8e2e0e109')
owm = pyowm.OWM('fca9e4262edac35767e09e053c4c76d0')

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
    #if(not verified):
     #   authStart()
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Yes Sir?')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        # engine.say('You said: ' + command)
        # engine.runAndWait()
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();


    return command





def assistant(command):
    "if statements for executing commands"
    if 'jarvis' in command:
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
        #Get time
        elif 'time' in command:
             now = datetime.now()
             talkToMe("It is " + now.strftime('%I:%M %p'))

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
                talkToMe("The date is "+ month + " 1st, " + strftime("%Y"))
            elif(strftime("%d")=="2"):
                talkToMe("The date is "+ month + " 2nd, " + strftime("%Y"))
            elif(strftime("%d")=="3"):
                talkToMe("The date is "+ month + " 3rd, " + strftime("%Y"))
            elif(strftime("%d")=="21"):
                talkToMe("The date is "+ month + " 21st, " + strftime("%Y"))
            elif(strftime("%d")=="22"):
                talkToMe("The date is "+ month + " 22nd, " + strftime("%Y"))
            elif(strftime("%d")=="23"):
                talkToMe("The date is "+ month + " 23rd, " + strftime("%Y"))
            else:
                talkToMe("The date is " + month + strftime("%d") + ", " + strftime("%Y"))
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

        elif 'weather in' in command:
            reg_ex = re.search('weather in (.*)', command)
            if reg_ex:
                city = reg_ex.group(1)
                weather = Weather()
                location = geolocator.geocode(city)
                placeweather = location.latitude, location.longitude
                #Get weather
                observation = owm.weather_at_place(city)
                w = observation.get_weather()
                currentTemperature = w.get_temperature('celsius')
                tempCelsius = int(currentTemperature['temp']) * 1.8
                tempFahrenheit = tempCelsius + 32
                tempFahrenheit = str(tempFahrenheit)
                talkToMe("It is "+tempFahrenheit + " degrees Fahrenheit")
                print ("It is "+tempFahrenheit + " degrees Fahrenheit")


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
            else:
                talkToMe('I don\'t know what you mean!')
        elif 'alarm' in command:
            reg_ex = re.search('set alarm for (.*)', command)
            if reg_ex:
                time = reg_ex.group(1)
                now = datetime.now()
                completeAmPm = ""
                AmPmCommand=now.strftime('%p')
                for letter in AmPmCommand:
                    completeAmPm = completeAmPm + letter.lower() + "."
                alarm.alarm(time, completeAmPm)



#loop to continue executing multiple commands

while True:
#     if(authenticated):
    assistant(myCommand())
