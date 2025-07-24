'''
A string is a group of letters / words or sentences
'''

name = 'Viktor'
country = 'India'

# 1. Find number of characters of a string
print(len(name)) # Output is 6

# 2. To print a particular character of a string
print(name[0]) # Output V since indexing begins from 0, 1, 2 ....
print(name[-1]) # Prints the last character 'r'
print(name[0:1]) # prints only v, if it is between 0 -> 1 then it does not prints 1
print(name[0:]) # prints full 

# 3. Functions of a string 
username = input('Enter your name: ')
print('Uppercase of your name is: ', username.upper())
print('Length of your name string is: ', len(username))
print('First letter of your string is: ', username[0])
print('Here is your username replaced by AI: ', name.replace('Viktor', 'AI'))