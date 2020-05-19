'''
HRA is 10% of Basic Salary
DA is 20% of Basic Salary
TA is 10% of Basic Salary
PF is 20 % of Basic Salary
'''
salary = int(input("Enter your Salary: "))
hra =+ (salary * 10) / 100
da =+ (salary * 20) / 100
ta =+ (salary * 10) / 100
pf =+ (salary * 20) / 100
print("Net Salary is: "+str(salary-hra-da-ta-pf))
