# Simple Calculator using match case 

operator = input('Please enter the operation to perform: +, -, *, /')
match operator: # Match statement for operator 

    case '+': # The case for addition 
        num1_add = int(input('Please enter first number: '))
        num2_add = int(input('Please enter second number: '))
        sum = num1_add + num2_add
        print('The sum is: ',sum)

    case '-': # the case for subtraction 
        num1_sub = int(input('Please enter the first number: '))
        num2_sub = int(input('Please enter the second number: '))
        difference = num1_sub - num2_sub
        if(difference<0):
            print('The difference is', difference,'and is a negative number')
        else:
            print('The difference is', difference)
            
    case '*':
        num1_mul = int(input('Please enter the first number: '))
        num2_mul = int(input('Please enter the second number: '))
        product = num1_mul * num2_mul 
        print('The product is', product)
    case '/':
        num1_div = int(input('Please enter the first number: '))
        num2_div = int(input('Please enter the second number: '))
        ans = num1_div/num2_div
        print('The answer is', ans)

# End of program 