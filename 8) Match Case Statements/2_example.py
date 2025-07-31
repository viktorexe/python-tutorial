# A simple match case program to match day of the week corresponding to its serial number

day_num = int(input('Please enter the number: '))

match day_num:
    case 1:
        print('You entered 1 and the day is Monday')
    case 2: 
        print