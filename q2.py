stock_name = input("Enter stock name: ")
price = float(input("Enter stock price: "))
sell = float(input("Enter sell price: "))
no_of_units =  int(input("Enter number of units: "))
profit =  (sell - price) * no_of_units
print("You have made a profit of :  ", profit)  