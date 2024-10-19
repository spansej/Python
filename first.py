print("Hello Spansej!!")

#this is a single line comment


'''
multi line comment
or u can use double  quotes
In py everything is a object
var is a reference to obj of class int 
type is a method or function to know the data type of var
'''
#variable = literal
var = 10
#variable names are case sensitive so var and VAR are diff variables
print(type(var))
print(var)

#type conversion 
#implicit typecasting will always do an upcast
print(3/2.0)

#for integer division
print(3//2)

#explicit typecasting 
var_num = '1111'
print(type(var_num))
print(type(int(var_num)))

a = input("Please  enter a number: ")
print(a)

list1=[1,2,3,4]
list2=[1,2,3,4]
if(list1==list2):
    print("list1 and list2 are equal")
else:
    print("list1 and list2 are not equal")
    
list3=list1

if(list1 is list3):
    print("same address")
    print(id(list1))
    print(id(list3))
else:
    print("different address")
    print(id(list1))
    print(id(list3))
    
    if(list1 is not list2):
        print("same address")
        print(id(list1))
        print(id(list3))
    else:
        print("different address")
        print(id(list1))
        print(id(list3))