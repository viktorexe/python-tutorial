# Nested Loops
# In this we will take a number as input and print statements on basis of it

num = int(input('Please enter a number: '))
if(num<0):
    print('Entered number is negative')
elif(num>0):
    if(num >= 1 and num <= 5):
        print('Entered number lies between 1-5')
    if(num>5 and num<=10):
        print('Number lies between 6-10')
    else:
        print('Number is greater than 10')
else:
    print('Number os 0')