# Python program to find current  
# weather details of any city 
# using openweathermap api 
  
# import required modules 
import requests, json 
  
# Enter your API key here 
api_key = "4fd6a6bb4f5a530374696069ffa8277d"
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

def getTemperature(city):
	city_name = city
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
	response = requests.get(complete_url) 
	x = response.json() 
	
	if x["cod"] != "404": 
		y = x["main"] 
		current_temperature = y["temp"] 
		z = x["weather"] 
		weather_description = z[0]["description"]
		print("Made it to temp")
		return(str(round(int((current_temperature) * 9/5) - 459.67)))
	
	else: 
		return("City Not Found")

def getPressure(city):
	city_name = city
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
	response = requests.get(complete_url) 
	x = response.json() 
	
	if x["cod"] != "404": 
		y = x["main"] 
		current_pressure = y["pressure"] 
		z = x["weather"] 
		weather_description = z[0]["description"] 
		return(str(current_pressure))
	
	else: 
		return("City Not Found")

def getHumidity(city):
	city_name = city
	complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
	response = requests.get(complete_url) 
	x = response.json() 
	
	if x["cod"] != "404": 
		y = x["main"] 
		current_humidiy = y["humidity"] 
		z = x["weather"] 
		weather_description = z[0]["description"] 
		return(str(current_humidiy))
	
	else: 
		return("City Not Found")