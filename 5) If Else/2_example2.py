# Budget 

budget = 200
apple_price = int(input("Enter apple price: "))
if(budget>=apple_price):
    print('I can buy an apple, remaining amount is',budget-apple_price)
else:
    print("Your budget is low")