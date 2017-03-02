"""
this is a class to create the rooms
there has to be a better way to do this
"""


class Room(object):
    def __init__(self, x, y, north, east, south, west, color=(255, 0, 0) ):
        self.x = x
        self.y = y
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.color = color

       '''set up setter method in this class...Room1's south is Room2's north, room3's west is room2's east ect...
        #  for a SLL = the only thin a room knows is what room is next'''

    def setconnection(self):
        return self.setconnection

















