'''
Author: Hope Wagner
Date: 05 Apr 2025
HackKU 2025
Last modified: 05 Apr 2025
Purpose: Room class for individual rooms. The Map class contains and manages these.
'''
# TODO: Member functions, test

#from grid import Grid

class Room:
    def __init__(self,row,col,desc="LOREM IPSUM"):
        self.desc = desc        #To be set upon creation; the placeholder is painfully obvious.
        #self.tile_str = ""
        #self.grid = Grid()
        self.pos = [row,col]
        self.is_visit = False

        #Refers to other Rooms directly. (Might be bad for memory, might not...)
        self.directions = {
            "north": None,
            "east": None,
            "south": None,
            "west": None
        }

        #Which actions are available in the room.
        self.actions = {
            "pickup": False     #Pick up available items
        }

        #List of item names; Exec uses item names to determine Item behaviour
        self.items = []

        #List of character names; Exec uses item names to determine Character behaviour
        self.characters = []

        def is_visited(self):
            '''Returns whether the room has been visited.'''
            return is_visit

        def visit(self):    #Move to Map class?
            '''Marks the room as visited.'''
            is_visit(True)

        def add_item(item_name):
            '''Adds the specified item name to the Room's items.'''
            pass

        def remove_item(index):
            '''Removes the specified item name from the room and returns it.'''
            pass
