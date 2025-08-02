name = 'Viktor'
for i in name:
    print(i)

'''
Code Explanation:
for i in name: Here i is referred to as index, 
one by one index value shifts in the string till the end, 
similary different for list
goes from v->r one by one 
'''

list = ['hi', 'hello', 12]
for i in list:
    print(i) # Prints every object in the list 

# We can add more nesting in it, if we want to print something over an index
country ='India'
for i in country:
    print(i)
    if(i=='I'):
        print('This is something special')
