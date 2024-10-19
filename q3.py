employee_name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))
increment_percentage =  float(input("Enter increment percentage: "))
increment_amount = (salary * increment_percentage) / 100
new_salary=salary+increment_amount
print("\"Dear",employee_name,"your salary is ",salary," rs and you have a increment of",increment_percentage,"percentage so congratulations you now have your new salary as",new_salary,' rs"')