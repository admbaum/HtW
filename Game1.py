'''
This is the class file for the board.  It will govern what the board looks like and doors that the player and opponent
can go through and the start location of the player and opponent.
'''

import pygame
import random

pygame.init()

xcoord = random.randrange(1, 800, 5)
print(xcoord)
ycoord = random.randrange(1, 600, 5)
print(ycoord)


while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break


    class TheBoard(object):
        def __init__(self, name):
            self.name = name
    #ycoord
    surface_sz = 800
    #xcoord
    surface_sz1 = 600

    main_surface = pygame.display.set_mode((surface_sz, surface_sz1))

    room = (ycoord, xcoord, 90, 90)
    roomcolor = (255, 0, 0)

    main_surface.fill((192, 192, 192))
    main_surface.fill(roomcolor, room)

    pygame.display.flip()
