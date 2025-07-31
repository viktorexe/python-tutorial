'''
Bonus Challenge (Mini Project Idea)
Basic Password Strength Checker
Input: password
Check:
Length < 6 → "Very Weak"
Only letters or only digits → "Weak"
Letters + digits → "Strong"
Length > 10 and mix → "Very Strong"
'''

password = input('Please enter your password: ')
if(password.isdigit()):
    print('Your password is weak')
elif(password.isalnum()):
    print('Your password is moderate with numbers and alphabets'):
elif(password.isalnum()):
    if(len(password))