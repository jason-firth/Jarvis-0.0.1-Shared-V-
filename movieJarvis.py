import os
movieInput = input("What Movie?: \n").replace(" ", "")
directory = "/"
movies = {}
moviesList = []
filetypes = ["mp4","mp3", "m4v"]
print(os.listdir(directory))
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
	os.system("vlc " + movies[movieToPlay] + " --fullscreen --play-and-exit")
else:
	print("That does not exist")


# FOR JARVIS: change print to talkToMe