# Strings are immutable, existing strings never change, it makes a new string

a = 'mango'
b = 'Banana!!!'
c = 'Welcome to the consle!!'
d = 'hello hello everyone'
print(len(a)) # Prints Length of a
print(a.upper()) # Fully capatilizes the string
print(a.lower()) # Changes to string to lowercase
print(a.capitalize()) # Converts everything to lowercase and only capitalizes the first letter of the string
print(a.replace('Mango', 'Apple')) # Replaces the character(s) in the string and returns a modified string 
print(b.rstrip('!')) # Removes unwanted characters from strings (does not work for the ones before string)
print(c.rstrip('!'))
print(c.endswith('!')) # To c
print(c.center(50)) # Shifts the text to centre with 50 blank spaces on left
print(d.count('hello')) # Counts the numebr of time the thing appears in the string
