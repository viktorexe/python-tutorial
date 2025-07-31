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
if(password==int):
    print('Your password is weak and has only numbers:')
    if(password == int and password.isalphanum()):
        print('Your password is medium strength and has numbers and letters')
else:
    print('idk')