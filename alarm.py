from time import gmtime, strftime
import pyttsx3

engine = pyttsx3.init()
def alarm(endTime, ampm):
	if((now.strftime('%I:%M') + ampm) == endTime):
		if(ampm == "a.m."):
			engine.say('Good morning sir, this is you alarm for ' + now.strftime('%I:%M') + ampm)
    		engine.runAndWait()
    	else:
    		engine.say('Good afternoon sir, this is you alarm for ' + now.strftime('%I:%M') + ampm)
    		engine.runAndWait()




