'''
Input: A string ("red", "yellow", "green")
Output:
red → "Stop"
yellow → "Slow down"
green → "Go"
anything else → "Invalid color"
'''

color = input('please enter the color: ').lower() # To lowercase the entered string in case user enters Red instead of red

match color: # Match statement for color
    
    case 'red': # If the user enters red in the input
        print('Red light means stop')

    case 'yellow': # If the user enters yellow in the input
        print('Yellow means slow')
    
    case 'green': # If the uer enters green in the input
        print('Green means go')

    case _: # If the user enters none of the above color
        print(color, 'is not a color in traffic light')

# End of program    