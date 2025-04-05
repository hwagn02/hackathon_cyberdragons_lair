'''
Author: Hope Wagner
Date: 05 Apr 2025
HackKU 2025
Last modified: 05 Apr 2025
Purpose: Class to store an array of values; grid starts at 0,0 in top left. Size is preset w/ val_init.
'''
# TODO: Should be done!

class Grid:
    def __init__(self,row=0,col=0,val=None):
        self.grid = []
        self.num_rows = row
        self.num_cols = col
        
        '''Initializes the Grid as an array of the specified value and size.'''
        for i in range(self.num_rows):
            row_list = []
            for i in range(self.num_cols):
                row_list.append(val)
            self.grid.append(row_list)

    # def val_init(self,row=0,col=0,val=None):
        

    def get_val(self,row,col):
        '''Returns the value at the given position.'''
        if self.is_valid_pos(row,col):
            return self.grid[row][col]
        else:
            raise IndexError("Position out of range.")

    def set_val(self,row,col,val):
        '''Sets the value to val at the given position.'''
        if self.is_valid_pos(row,col):
            self.grid[row][col] = val
        else:
            raise IndexError("Position out of range.")

    def is_valid_pos(self,row,col):
        '''Determines if the given value is a valid position.'''
        if row >= 0 and row < self.num_rows and col >= 0 and col < self.num_cols:
            return True
        else:
            return False

    def __str__(self):
        '''Converts the Grid into a printable string.'''
        grid_str = ""
        for row in self.grid:
            for i in range(len(row)):
                grid_str += str(row[i])
            grid_str += '\n'

        return grid_str
        

            
