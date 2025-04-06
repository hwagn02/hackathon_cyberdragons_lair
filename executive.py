'''
Author: Hope Wagner
Date: 05 Apr 2025
HackKU 2025
Last modified: 06 Apr 2025
Purpose: Executive class to run game.
'''
# TODO: Add Inventory & item functionality, Characters, etc...

from room_map import Map

class Executive:
    def __init__(self,char):
        #Map of Rooms, currently a 3x3 grid.
        self.map = Map(3,3,1,0)
        self.map.player_char = char

        #Flags denote states of various parts of the game.
        self.flags = {
            "state": None,  #What state the game is currently in.
            "run": False    #Whether or not the game is running.
        }
        self.states = {"start","main","inventory","item","end"}
        self.directions = {"north","east","south","west"}
        #self.inventory = Inventory()
        self.option_dict = None

        # Initialization of map.
        self._map_init()

    def run(self):
        '''Runs the primary program, asking for user prompts and running class functions.'''
        self.flags["state"] = "main"
        self.flags["run"] = True

        #Loop for while game runs.
        while self.flags["run"] == True:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n————————————————————————————————")
            print(self.map)
            print("————————————————————————————————")
            print(self.map.get_active_room().desc + '\n')
            print(self.map.get_active_pos(), '\n')
            choice = self.user_options()
            self.do_action(choice)
            print("————————————————————————————————")

        #Code for game end.
        print("Program has ended. Goodbye!")

    def do_action(self,action):
        '''Executes a specified action.'''
        if action in self.directions:
            self.map.move(action)
        elif action == "pickup":
            print("\nYou don't seem to be able to pick up the item...")
            self._enter_cont()
        elif action == "exit":
            self.flags["run"] = False
            self.flags["state"] = "end"
        
    
    def user_options(self):
        '''Assembles available user options based on game state, asks for input, returns action name.'''
        self.option_dict = {}   #Consists of 1-character keys and names of actions for do_action.
        room = self.map.get_active_room()
        user_input = None
        state = self.flags["state"]

        #Action menu dependent on game state.
        if state == "main":
            #Actions include available directions, room actions, and inventory (not implemented)
            for direction in list(room.directions):
                if room.directions[direction] is not None:
                    self.option_dict.update({(direction[0]):direction}) #First character of action is used as key.

            for action in list(room.actions):
                if room.actions[action]:
                    self.option_dict.update({(action[0]):action})

            self.option_dict.update({'x':"exit"})

            #These determined whether a method was available
            '''
            if len(room.items) != 0:
                self.option_dict.update({'s':'search'})

            if len(room.characters) != 0:
                self.option_dict.update({'s':'talk'})
            '''
            
        elif state == "inventory":
            #Display available items to interact with (state=item) and exit (state=item)
            pass
        elif state == "item":
            #Display available item methods.
            pass
        
        user_input = input(self.print_user_options(self.option_dict))
            
        while user_input not in list(self.option_dict):
            print("\nInvalid input, please try again.\n")
            user_input = input(self.print_user_options(self.option_dict))
            
        return self.option_dict[user_input]
                
            

    def print_user_options(self,options,prompt="Select an option."):
        '''Receives a dict of inputs and options, then prints choices.'''

        input_str = prompt + '\n\n'
        for choice in list(options):
            input_str += '['+choice+']\t'+str(self.option_dict[choice])+'\n'

        return input_str + '\nChoice: '
            
    def _enter_cont(self):
        input("\nPress enter to continue.")
        print("\n")

    def print_map(self):
        '''Prints map of known locations.'''
        print(self.map)

    def _map_init(self):
        '''Initializes the map and its connections.'''
        #Presently borrowed from _test_room_map.py.
        self.map.link_room([0,0],[0,1],'east','west')
        self.map.link_room([0,0],[1,0],'south')
        self.map.link_room([0,1],[1,1],'south','north')
        self.map.link_room([1,1],[2,1],'south','north')
        self.map.link_room([1,0],[1,1],'east','west')
        self.map.link_room([1,1],[1,2],'east','west')
        #Possibly add methods to quick-set descs, items, etc. from text files?
        self.map.get_room(1,0).desc = "Where it all begins - the beginning."
        self.map.get_room(0,0).centre = 'k'
        self.map.get_room(0,0).add_item("key")
        self.map.get_room(0,0).actions["pickup"] = True
        self.map.get_room(0,0).desc = "Hey, wait, there's a key here!\nToo bad you can't pick it up yet..."
        #print(m)
