# Strings are immutable, existing strings never change, it makes a new string

a = 'mango\n'
b = 'Banana!!!'
c = 'Welcome to the consle!!'
d = 'hello hello everyone how are you'
e = 'ABCEDFGhijklmnop123'
f = ' '
g = 'Hello All'
print(len(a)) # Prints Length of a
print(a.upper()) # Fully capatilizes the string
print(a.lower()) # Changes to string to lowercase
print(a.capitalize()) # Converts everything to lowercase and only capitalizes the first letter of the string
print(a.replace('Mango', 'Apple')) # Replaces the character(s) in the string and returns a modified string 
print(a.isalpha()) # Returns True if the whole string is only A-Z or a-z, no white spaces, numbers or characters
print(a.islower()) # Returns True if the whole string is lowercase
print(a.isprintable()) # Returns True if everything in the string is printable
print(a.swapcase()) # Converts lowercase to uppercase and vice-versa 
print(b.rstrip('!')) # Removes unwanted characters from strings (does not work for the ones before string)
print(c.rstrip('!'))
print(c.endswith('!')) # To check if a given string ends with the entered character (returns True or False)
print(c.startswith('Welcome')) # To check if a given string starts with the entered character (returns True or False)
print(c.center(50)) # Shifts the text to centre with 50 blank spaces on left
print(d.count('hello')) # Counts the numebr of time the thing appears in the string
print(d.find('you')) # Finds the thing and returns with index number, if not found returns -1
print(e.isalnum()) # Returns True if the string has only A-Z, a-z, or numbers, no white spaces or any character
print(f.isspace()) # Returns True if the string only contains white spaces
print(g.istitle()) # Returns True if all words of string have first letter capitalized