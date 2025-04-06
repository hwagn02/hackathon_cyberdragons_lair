'''
Author: Hope Wagner
Date: 05 Apr 2025
HackKU 2025
Last modified: 06 Apr 2025
Purpose: Main function to run Executive and begin program.
'''
# TODO: Write!

from executive import Executive

def main():
    '''Runs an Executive, simple as that.'''
    my_exec = Executive(input("Welcome to Cyberdragon's Lair!\nEnter a Player Character: ")[0])
    my_exec.run()
    
if __name__ == "__main__":
    main()
