# A simple match case program to match day of the week corresponding to its serial number

day_num = int(input('Please enter the number: '))

match day_num:
    case 1:
        print('You entered 1 and the day is Monday')
    case 2: 
        print('You entered 2 and the day is Tuesday')
    case 3: 
        print('you entered 3 and the day is Wednesday')
    case 4: 
        print('You entered 4 and the day is Thursday')
    case 5: 
        print('You entered 5 and the day is Friday')
    case 6: 
        print('You entered 6 and the day is Saturday')
    case 7: 
        print('you entered 7 and the day is Sunday')
    case _: # Using _ means default case, just like 'else' in if else statements 
        print('There are 7 days in a week, enter a number between 1-7')

# End of program 