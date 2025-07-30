# Strings are immutable, existing strings never change, it makes a new string

a = 'mango'
b = 'Banana!!!'
print(len(a)) # Prints Length of a
print(a.upper()) # Fully capatilizes the string
print(a.lower()) # Changes to string to lowercase
print(a.capatilize()) # Converts everything to lowercase and only capitalizes the first letter of the string
print(a.replace('Mango', 'Apple')) # Replaces the character(s) in the string and returns a modified string 
print(b.rstrip('!')) # Removes unwanted characters from strings (does not work for the ones before string)
