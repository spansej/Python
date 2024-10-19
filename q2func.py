def profit(sell,price,no_of_units):
    profit =  (sell - price) * no_of_units
    return profit
     


stock_name = input("Enter stock name: ")
price = float(input("Enter stock price: "))
sell = float(input("Enter sell price: "))
no_of_units =  int(input("Enter number of units: "))

print("You have made a profit of :  ",profit(sell,price,no_of_units))