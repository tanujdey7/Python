#(C) GitHub.com/tanujdey7
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))
if(num1 > num2 and num1 > num3):
    print("Number 1 is greater")
elif(num2 > num3 and num2 > num1):
    print("Number 2 is greater")
else:
    print("Number 3 is greater")
    
