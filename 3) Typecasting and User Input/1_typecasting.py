'''
Typecasting means to convert one datatype to other
string to integer
interger to string
'''

a = '99'
b = int(a)
print(b + 10)

x = 99
y = str(x)
print("Value is "+ y)

f = 5.9
i = int(f)
print(i)    # Output: 5 (decimal hata diya)

print(bool(0))       # False
print(bool(10))      # True
print(bool(""))      # False
print(bool("hello")) # True

# NOTE - Boolean returns True if something exist and false of there is nothing or 0
'''
x = "abc"
y = int(x)     # ❌ Error: because "abc" is not a number
'''