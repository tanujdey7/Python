#Github.com/tanujdey7
try:
    age = int(input("Enter Age: "))
except Exception as e:
    print(e)
else:
    if age > 18:
        print("Can Vote")
    else:
        print("Cannot Vote")
finally:
    print("Bye!!")
