def calc(dollar):
    rupees =  dollar * 82
    return rupees
dollar = float(input("Enter amount in dollars: "))
result=calc(dollar)
print(f"You have {dollar} dollars and {result} rupees")