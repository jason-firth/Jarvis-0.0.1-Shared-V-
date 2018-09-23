from time import gmtime, strftime
import pyttsx3
from datetime import date, timedelta
from datetime import datetime



engine = pyttsx3.init()
def alarmjarvis(endTime, ampm):
	alarmGoing = True
	print("confirm set alarm for " + endTime)
	while True:
		now = datetime.now()
		if((now.strftime('%I:%M ') + ampm) == endTime):
			if(alarmGoing == "True"):
				if(ampm == "a.m."):
					engine.say('Good morning sir, this is you alarm for ' + now.strftime('%I:%M') + ampm)
					engine.runAndWait()
					alarmGoing = False
				else:
					engine.say('Good afternoon sir, this is you alarm for ' + now.strftime('%I:%M') + ampm)
					engine.runAndWait()
					alarmGoing = False