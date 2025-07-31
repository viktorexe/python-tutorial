'''
Name & Age Checker
Input: Name and Age
If age >= 18, print "Hi [Name], you are an adult"
Else if age < 10, print "Hello little [Name]!"
Else "Hey [Name], you are a teenager"
'''

print('Name & Age Checker')
name = input('Please enter your full name: ')
age = int(input('Please enter your age: '))

if(age>=18):
    print('Hi', name, 'you are an adult')
elif(age<10):
    print('Hello little', name)
else:
    print('Hello', name, 'you are a teenager')