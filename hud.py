import sys
import pygame
import pygame.camera
import asyncio

async def main():
	pygame.init()
	pygame.camera.init()

	#create fullscreen display 640x480
	screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN)

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

		# check for quit events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				webcam.stop()
				pygame.quit()
				sys.exit()
def stophud():
	webcam.stop()
	pygame.quit()
	sys.exit()

asyncio.run(main())

