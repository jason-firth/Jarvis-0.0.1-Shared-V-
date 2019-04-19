import os
movieInput = input("What Movie?: \n")
directory = "/media/pi/8891-D645/"
movies = {}
moviesList = []
filetypes = ["mp4","mp3", "m4v"]
print(os.listdir(directory))
for movie in os.listdir(directory):
	if("." in movie):
		if(movie.split(".")[1] in filetypes):
			print(movie.split(".")[1])
			pathToMovie = directory+movie
			movies[movie.split('.')[0]] = pathToMovie
			moviesList.append(movie.split('.')[0].replace("_", " ").upper())
# FOR JARVIS: change movieToPlay to command.split("play")[1]
movieToPlay = movieInput
if(movieToPlay in moviesList):
	os.system(movies[movieToPlay])
else:
	print('That does not exis')
# FOR JARVIS: change print to talkToMe