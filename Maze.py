from Room import Room


class Maze(object):

    def __init__(self):
        self.head = None

    def generate_maze(self):
        room1 = Room(250, 250, None, None, None, None)
        room2 = Room()
        room3 = Room()
        room4 = Room()
        room5 = Room()
        room6 = Room()
        room7 = Room()
        room8 = Room()

        room1.setconnection(None, room2, room3, None)
        room2.setconnection(None, None, room4, room3)
        room3.setconnection(room1, room4, None, None)
        room4.setconnection(room2, room5, None, room3)
        room5.setconnection(None, room4, room6, None)
        room6.setconnection(room5, None, None, room7)
        room7.setconnection(room8, room6, None, None)
        room8.setconnection(None, None, room7, None)

# Room set up
# room1.Room.setnorth(None)
# room1.Room.seteast(room2)
# room1.Room.setsouth(room3)
# room1.Room.setwest(None)

# room2.Room.setnorth(None)
# room2.Room.seteast(None)
# room2.Room.setsouth(room4)
# room2.Room.setwest(room3)

# room3.Room.setnorth(room1)
# room3.Room.seteast(room4)
# room3.Room.setsouth(None)
# room3.Room.setwest(None)

# room4.Room.setnorth(room2)
# room4.Room.seteast(room5)
# room4.Room.setsouth(None)
# room4.Room.setwest(room3)

# room5.Room.setnorth(None)
# room5.Room.seteast(room4)
# room5.Room.setsouth(room6)
# room5.Room.setwest(None)

# room6.Room.setnorth(room5)
# room6.Room.seteast(None)
# room6.Room.setsouth(None)
# room6.Room.setwest(room7)

# room7.Room.setnorth(room8)
# room7.Room.seteast(room6)
# room7.Room.setsouth(None)
# room7.Room.setwest(None)

# room8.Room.setnorth(None)
# room8.Room.seteast(None)
# room8.Room.setsouth(room7)
# room8.Room.setwest(None)
