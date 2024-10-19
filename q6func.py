def calc(fare,discount_rate):
    final_rate = fare - (fare *  discount_rate / 100)
    return final_rate
source = input("Enter source: ")
destination = input("Enter destination: ")
fare = float(input("Enter fare in INR: "))
discount_rate = int(input("Enter discount rate percentage: "))
result=calc(fare,discount_rate)
print(f"Your fare from {source} to {destination} is {fare} INR and  after discount of {discount_rate}% it will be {result} INR")