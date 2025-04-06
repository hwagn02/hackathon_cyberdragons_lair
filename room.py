'''
Author: Hope Wagner
Date: 05 Apr 2025
HackKU 2025
Last modified: 05 Apr 2025
Purpose: Room class for individual rooms, which link to other Rooms in four directions (or more if needed).
         The Map class contains and manages these.
'''
# TODO: Test w/ Map, add more self.actions options, add tile code

from grid import Grid

class Room:
    def __init__(self,row,col,desc="LOREM IPSUM",centre=' '):
        self.desc = desc        #To be set upon creation; the placeholder is painfully obvious.
        self.pos = [row,col]    #Are methods really needed to get these? User shouldn't interact directly... 
        self.is_visit = False

        #Refers to other Rooms directly. (Does not appear to duplicate the Room.)
        self.directions = {
            "north": None,
            "east": None,
            "south": None,
            "west": None
        }

        #Initial build of Tile.
        #self.tile = Grid(3,5, ' ')
        self.centre = centre
        #self.make_tile()
        
        #Which actions are available in the room. Define more later.
        self.actions = {
            "pickup": False     #Pick up available items
        }

        #List of item names; Exec uses item names to determine Item behaviour
        self.items = []

        #List of character names; Exec uses item names to determine Character behaviour
        self.characters = []

    def is_visited(self):
        '''Returns whether the room has been visited.'''
        return self.is_visit

    def visit(self):    #Move to Map class?
        '''Marks the room as visited.'''
        self.is_visit = True

    def set_dir(self,direction,room):
        '''Sets a particular direction to refer to another Room or None.'''
        if (direction in self.directions.keys()):
            if isinstance(room,Room) or room is None:
                self.directions[direction] = room
            else:
                raise ValueError("Room must be linked to another Room or None.")
        else:
            raise IndexError("Direction "+str(direction)+" is not a valid key.")

        # This process creates a reference to the original linked Room;
        # changes to the original change the values returned by the linked version, and vice versa.

    def get_dir(self,direction):
        '''Returns the Room in a particular direction, or None if None.'''
        if (direction in self.directions.keys()):
            return self.directions[direction] == room
        else:
            raise IndexError("Direction "+str(direction)+" is not a valid key.")

    def is_open_dir(self,direction):
        '''Determines if a particular direction is valid for movement.'''
        if direction in list(self.directions):
            return isinstance(self.directions[direction],Room)
        else:
            return False

    def add_item(self,item_name:str):
        '''Adds the specified item name to the Room's items.'''
        self.items.append(item_name)

    def remove_item(self,index):
        '''Removes the specified item from the room and returns its name.'''
        return self.items.pop(index)

    #Handled in Map class.
    '''def make_tile(self,centre=" "):
        #Rebuilds and sets the tile based on current directions and centre.
        self.tile = Grid(3,5, ' ')
        self.tile.set_val(0,0,'┌')
        self.tile.set_val(0,4,'┐')
        self.tile.set_val(2,0,'└')
        self.tile.set_val(2,4,'┘')
        
        if self.is_open_dir["north"]:
            pass
        else:
            pass

        if self.is_open_dir["east"]:
            pass
        else:
            pass

        if self.is_open_dir["south"]:
            pass
        else:
            pass

        if self.is_open_dir["west"]:
            pass
        else:
            pass'''

        

    '''def __str__(self):
        #Returns reconstructed tile based on available directions and centre.

        pass'''
