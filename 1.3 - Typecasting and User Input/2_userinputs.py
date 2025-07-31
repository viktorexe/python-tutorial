'''
Inputs are used to take a value as an input from the user
You cannot add integer to someone input which is of string
Integers can be added to integer inputs only 
'''

# 1. String Inputs
name = input('Please enter your name: ')
print('Your name is:', name )

# 2. Integer input
age = int(input('Please enter your age: '))
print('Your age is:', age)

# 3. Float Input
height = float(input('Please enter your height (in feet): '))
print('You height is:', height,'feet')

# 4. Adding int to integer inputs
current_age = int(input("Please enter your current age: "))
print('Your age next year will be: ', current_age + 1)

# 5. To take two values in one input at once
value1, value2 = input('Please enter 2 values you want to add: ').split()
value1 = int(value1)
value2 = int(value2)
print(value1 + value2)

# 6. Multiple different inputs at once
username = input('Please enter your name: ')
userage = int(input('Please enter your age: '))
print("Hello", username,'you are', userage,'years old')

# 7. Combining 2 string inputs 
firstname = input('Please enetr your first name: ')
surname = input('Please enter your surname: ')
print('Your full name is:', firstname, surname)

# 8. Combining two integer inputs and printing the sum 
num_1 = int(input('Please enter first number: '))
num_2 = int(input('Please enter second number: '))
print('Their sum is: ', num_1+num_2)