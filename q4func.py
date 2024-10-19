def calc(height):
    height_in_foot =  height / 30.48
    return height_in_foot
    
height = int(input("Enter height in cm "))
result=calc(height)
print(f"Height in feet is {result} feet")