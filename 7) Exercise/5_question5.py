'''
Digital Clock Style Greeting
Input: Hour (0 to 23)
Output:
0-11: "Good Morning!"
12-16: "Good Afternoon!"
17-20: "Good Evening!"
21-23: "Good Night!"
⚠️ Invalid hour → "Invalid time!"
'''

time = int(input('Please enter the time between 0-23 hrs: '))
if(time>=0 and time <=11):
    print('Good morning')
elif(time>=12 and time <=16):
    print('Good afternoon')
elif(time>=17 and time<=20):
    print('Good evening')
else:
    