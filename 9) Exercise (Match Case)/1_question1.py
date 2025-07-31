# Simple Calculator using match case 

operator = input('Please enter the operation to perform: +, -, *, /')
match operator: # Match statement for operator 
    case '+':
        num1 = int(input('Please enter first number: '))
        num2 = int(input('Please enter second number: '))
        sum = num1 + num2
        print('The sum is: ',sum)