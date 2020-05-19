#Github.com/tanujdey7
try:
    num = int(input("Enter Number: "))
    if num < 0:
        raise ValueError("Positive number daal be")
    else:
        print(num)
except Exception as e:
    print(e)
