'''
Input: A string ("red", "yellow", "green")
Output:
red → "Stop"
yellow → "Slow down"
green → "Go"
anything else → "Invalid color"
'''

color = input('please enter the color: ')

match color: # Match statement for color
    
    case 'red': # If the user enters red in the input
        print('Red light means stop')

    case 'yellow': # If the user enters yellow in the input
        print('Yellow means slow')
    
    case 'green': # If the uer enters green in the input
        