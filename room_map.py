'''
Author: Hope Wagner
Date: 05 Apr 2025
HackKU 2025
Last modified: 05 Apr 2025
Purpose: Class to store and modify a Grid of Rooms, as well as update a related image.
'''
# TODO: Write member functions, possibly implement printable map?

from grid import Grid
from room import Room

class Map:
    def __init__(self,row,col,init_row,init_col):
        self.room_map = Grid(row,col)
        self.active_pos = [init_row,init_col]
        self.active_room = self.room_map.get_val(init_row,init_col)
        #self.img_map = Grid(row,col)   Constructed from Room's tile Grid

    def get_pos(self):
        '''Returns the active position.'''
        return self.active_pos

    def get_room(self):
        '''Returns the active Room object.'''
        return self.active_room

    #def add_tile(self):
        '''Adds active Room's tile to the img_map.'''

    #def __str__(self):
        '''Returns the current img_map.'''
        #return str(self.img_map)
        
