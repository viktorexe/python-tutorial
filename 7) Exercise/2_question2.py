'''
Grade Calculator (using elif)
Input: Marks (0-100)
Output:
90-100 → A
70-89 → B
50-69 → C
<50 → Fail
'''

print('Grade Calculator')
grades = int(input('Please enter your grades in integer: '))
if(grades>=90 and grades<=100):
    print('Youhave got an A grade')
elif(grades>=70 and grades <=89):
    print('You have got a B grade')
elif(grades>=50 and grades<=69):
    print('You have got a C grade'