#(C) Copyright GitHub.com/tanujdey7
name = input("Enter Name: ")
rollno = int(input("Enter Roll No: "))
maths = int(input("Enter Marks of Maths: "))
science = int(input("Enter Marks of Science: "))
english = int(input("Enter Marks of English: "))
print("Name is: "+name)
print("Maths: "+str(maths))
print("Science: "+str(science))
print("English: "+str(english))
total = maths+science+english
print("Total: "+str(total))
print("Percentage: "+str(total/3))
