import sys, pygame
from random import *


class MyBallClass(pygame.sprite.Sprite): # define a sprite
	def __init__(self, image_file, location, speed): # initiate the sprite
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image_file) # load the pic
		self.rect = self.image.get_rect()
		self.rect.left, self.rect.top = location # set the location of the sprite
		self.speed = speed # movement speed

	def move(self): # how to move
		self.rect = self.rect.move(self.speed) # moving the sprite
		# bouncing on walls
		if self.rect.left < 0 or self.rect.right > width:
			self.speed[0] = - self.speed[0]

		if self.rect.top < 0 or self.rect.bottom > height:
			self.speed[1] = - self.speed[1]

def animate(group): # animate a group of balls
	screen.fill([255, 255, 255])
	for ball in group:
		group.remove(ball)
		# check whether a ball touches another ball
		if pygame.sprite.spritecollide(ball, group, False):
			ball.speed[0] = -ball.speed[0]
			ball.speed[1] = -ball.speed[1]

		group.add(ball)
		ball.move() # move the ball
		screen.blit(ball.image, ball.rect) # draw the ball
	pygame.display.flip() # update
	pygame.time.delay(20)


pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size) # screen dimensions
screen.fill([255, 255, 255])
img_file = 'beach_ball.png' # image file for the ball
group = pygame.sprite.Group() # creating a group of balls

# creating a 3 by 3 array of balls
for row in range(0, 3):
	for column in range(0, 3):
		location = [column * 180 + 10, row * 180 + 10] # location of the ball
		speed = [choice([-2, 2]), choice([-2, 2])] # set the speed
		ball = MyBallClass(img_file, location, speed)
		group.add(ball)

# main loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # end the loop when receiving a quit signal
			running = False
	animate(group) # animate the group of balls
pygame.quit() # quit