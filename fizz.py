num=int(input("Enter a number: "))
# if(num%3==0 and num%5==0):
#     print("Fizz Buzz")
# elif(num%3==0):
#     print("Fizz")
# elif(num%5==0):
#     print("Buzz")
# else:
#     print("Invalid Input")
    
if(num%3==0 or num%5==0):
    if(num%3==0 and  num%5!=0):
        print("Fizz")
        if(num%3==0 and num%5==0):
            print("Fizz Buzz")
        else:
            if(num%5==0):
                print("Fizz")
    else:
        print("Buzz")
else:
        print("Invalid")
    
    