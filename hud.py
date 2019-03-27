import sys
import pygame
import pygame.camera
import os
pygame.init()
pygame.camera.init()
#create fullscreen display 640x480
screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN)
string = ""
#find, open and start low-res camera
cam_list = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cam_list[0],(256, 144))
webcam.start()
while True:
	#grab image, scale and blit to screen
	imagen = webcam.get_image()
	imagen = pygame.transform.scale(imagen,(800, 480))
	screen.blit(imagen,(0,0))

	#draw all updates to display
	pygame.display.update()
	event = pygame.event.get()
	keys = pygame.key.get_pressed()
	# check for quit events

	if event.type == pygame.KEYDOWN:
		keys = pygame.key.get_pressed()
		key = pygame.key.name(event.key)  # Returns string id of pressed key.
		
		if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
			#if  # Include any other shift characters here.
			#else:
			string += key.upper()
		elif event.key == pygame.K_RETURN:  # Finished typing.
			command = "echo 'echo " + string +"' > jarvis"
			os.system(command)
			string = ""
			break
		elif event.key == pygame.K_SPACE:
			string += " "
			break
		elif key == "backspace":
			string = string[:len(string) - 1]
		else:
			string += key



