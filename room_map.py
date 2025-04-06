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
        for i in range(self.room_map.num_rows):
            for j in range(self.room_map.num_cols):
                self.room_map.set_val(i,j,Room(i,j))
        
        self.active_pos = [init_row,init_col]
        self.active_room = self.room_map.get_val(init_row,init_col)
        self.player_char = 'o'
        #self.img_map = Grid(row,col)   Constructed from each Room's tile Grid

    def get_active_pos(self):
        '''Returns the active position.'''
        return self.active_pos

    def get_active_room(self):
        '''Returns the active Room object.'''
        return self.active_room

    def get_room(self,row,col):
        '''Returns the Room at a given position.'''
        return self.room_map.get_val(row,col)

    def link_room(self,coord1:list,coord2:list,dir1,dir2=None):
        '''Links one room to another based on coordinates; if dir2 defined, links both rooms together.'''
        room1 = self.get_room(coord1[0],coord1[1])
        room2 = self.get_room(coord2[0],coord2[1])
        
        #Potentially define version to link adjacent tiles?
        room1.set_dir(dir1,room2)
        if dir2 is not None:
            room2.set_dir(dir2,room1)

    def move(self,direction):
        '''Moves to a Room linked through the active Room if possible, and updates active position and Room visit status.'''
        if self.active_room.is_open_dir(direction):
            #self.draw_active_tile()
            self.active_room = self.active_room.directions[direction]
            self.active_pos = self.active_room.pos
        else:
            pass        #Don't know what to do if move is invalid...

        if not self.active_room.is_visited():
            self.active_room.visit()

        #self.draw_active_tile()

    #def draw_active_tile(self,centre=None):
        '''Adds active Room's tile to the img_map.'''

    def __str__(self):
        '''Returns the current img_map.'''
        str_map = ""

        #Iterates thrice for top, middle, and bottom of each corridor.
        for row in self.room_map.grid:

            #Top
            for room in row:
                if room.is_visited:
                    if room.is_open_dir("north"):
                        str_map += "┌   ┐"
                    else:
                        str_map += "┌───┐"
                else:
                    str_map += "     "

            str_map += '\n'

            #Middle
            for room in row:
                if room.is_visited:
                    if room.is_open_dir("west"):
                        str_map += "  "
                    else:
                        str_map += "| "

                    if room is self.active_room:
                        str_map += self.player_char
                    else:
                        str_map += room.centre

                    if room.is_open_dir("east"):
                        str_map += "  "
                    else:
                        str_map += " |"
                        
                else:
                    str_map += "     "
            
            str_map +='\n'

            #Bottom
            for room in row:
                if room.is_visited:
                    if room.is_open_dir("south"):
                        str_map += "└   ┘"
                    else:
                        str_map += "└───┘"
                else:
                    str_map += "     "
                
            str_map += '\n'

                
        return str_map
        
