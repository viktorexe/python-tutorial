# Type of integer, using elif

num = int(input('Please enter a number: ')) # Taking user input for a number

if(num>0):
    print(num,'is a positive number and greater than 0')
elif(num<0):
    print(num,'is a negative number and less than 0')
else:
    print(num,'is neither positive nor negative')
