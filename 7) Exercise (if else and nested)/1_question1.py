'''
Temperature Checker
Input: A number (temperature)
Task: Print:
"Cold Day" if below 15
"Pleasant" if 15-25
"Hot" if above 25
'''

print('Temperature Checker program!') 
temperature = float(input('Enter the temperature: ')) # Float input for temperature as it is decimal  
if(temperature<15):
    print('Cold Day')
elif(temperature>=15 and temperature<=25):
    print('Pleasant')
elif(temperature>=25):
    print('Hot')
