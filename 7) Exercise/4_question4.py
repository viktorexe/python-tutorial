'''
Odd or Even + Multiple of 5
Input: A numberPrint:
"Even and multiple of 5"
"Odd and multiple of 5"
"Even but not multiple of 5"
"Odd and not multiple of 5"
'''

number = int(input('Please enter a number: '))
if(number%2 == 0):
    if(number%5==0):
        print('The number is even and a multiple of 5')
    else:
        print('The number is even but not a multiple of 5')
if(number%2!=0):
    if(number%5==0):
        print('The number is odd and a multiple of 5')
    else:
        print('The number is odd but not a multiple of 5')