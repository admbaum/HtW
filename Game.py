#from Room import Rooms
from Maze import Maze
# This is the class file for the board.  It will govern what the board looks like and doors that the player and opponent
# can go through and the start location of the player and opponent.


import pygame

pygame.init()


class Game(object):
    def __init__(self): # when the game is initialized, I am creating Maze within it.
        _maze = Maze(0, 0)


# the beginning of the game loop
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                break

            surface_sz = 800
            surface_sz1 = 600
            main_surface = pygame.display.set_mode((surface_sz, surface_sz1))
            main_surface.fill((192, 192, 192))
            main_surface.fill(_maze.room_color(), _maze.room1())
            main_surface.fill(_maze.room_color(), _maze.room2())
            main_surface.fill(_maze.room_color(), _maze.room3())
            main_surface.fill(_maze.room_color(), _maze.room4())
            main_surface.fill(_maze.room_color(), _maze.room5())
            main_surface.fill(_maze.room_color(), _maze.room6())
            main_surface.fill(_maze.room_color(), _maze.room7())
            main_surface.fill(_maze.room_color(), _maze.room8())

            pygame.display.set_caption('Hunt the Wumpus')
            pygame.display.flip()

Game()
