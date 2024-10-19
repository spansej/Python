def new(salary,increment_percentage):
    increment_amount = (salary * increment_percentage) / 100
    new_salary=salary+increment_amount
    return increment_amount,new_salary


employee_name = input("Enter employee name: ")
salary = float(input("Enter employee salary: "))
increment_percentage =  float(input("Enter increment percentage: "))

result = new(salary,increment_percentage)
print("\"Dear",employee_name,"your salary is ",salary," rs and you have a increment of",increment_percentage,"percentage so congratulations you now have your new salary as",result[1],' rs"')
