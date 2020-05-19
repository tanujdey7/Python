#GitHub.com/tanujdey7
num = 4
try:
    if num%2!=0:
        raise ValueError("Sorry, Odd number")
    else:
        print("Even")
except Exception as e:
    print(e)
