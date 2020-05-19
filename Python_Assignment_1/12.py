num1 = 10
num2 = 20
print("Number 1: "+str(num1))
print("Number 2: "+str(num2))
num1 = num1 ^ num2
num2 = num2 ^ num1
num1 = num1 ^ num2
print("Number 1: "+str(num1))
print("Number 2: "+str(num2))