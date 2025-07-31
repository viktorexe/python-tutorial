# Simple Calculator using match case 

operator = input('Please enter the operation to perform: +, -, *, /')
match operator: # Match statement for operator 
    case '+':
        num1_add = int(input('Please enter first number: '))
        num2_add = int(input('Please enter second number: '))
        sum = num1_add + num2_add
        print('The sum is: ',sum)
    case '-':
        num1