#definition
def stock_profit(sell,price,no_of_units):
    return (sell - price) * no_of_units         #logic


#invocation
stock_name = input("Enter stock name: ")
price = float(input("Enter stock price: "))
sell = float(input("Enter sell price: "))
no_of_units =  int(input("Enter number of units: "))

total_profit=stock_profit(sell,price,no_of_units) #positional call
print("You have made a profit of :  ", total_profit)  