#GitHub.com/tanujdey7
try:
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))
    ans = num1/num2
    print(ans)
except ValueError:
    print("Enter Numeric Value")
except Exception as e:
    print("Can't Divide by Zero "+str(e))
