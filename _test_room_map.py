'''
Author: Hope Wagner
Date: 05 Apr 2025
HackKU 2025
Last modified: 05 Apr 2025
Purpose: Test file for Map class.
'''

from room_map import Map

def main():
    m = Map(3,3,0,0)
    #breakpoint()
    m.link_room([0,0],[0,1],'east','west')
    m.link_room([0,0],[1,0],'south')
    print(m)

    #breakpoint()
    #Test of basic movement.
    '''m.move('east')  #[0,1]
    m.move('east')  #Still [0,1]
    m.move('west') #[0,0]
    
    m.move('south') #[1,0]
    print(m)
    print(m.active_pos)
    
    m.move('north') #Still [1,0]
    print(m)
    print(m.active_pos)'''

    m.link_room([0,1],[1,1],'south','north')
    m.link_room([1,1],[2,1],'south','north')
    m.link_room([1,0],[1,1],'east','west')
    m.link_room([1,1],[1,2],'east','west')
    m.get_room(1,0).centre = 'k'
    m.get_room(1,0).add_item("key")
    print(m)   
            
    print(m.get_room(1,0).remove_item(0))
    
if __name__ == "__main__":
    main()
