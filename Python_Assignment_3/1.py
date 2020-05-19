# GitHub.com/tanujdey7
try:
    age = int(input("Enter age: "))
    print("Your age is: "+str(age))
except ValueError:
    print("Non numeric value")
finally:
    print("Bye")
    
