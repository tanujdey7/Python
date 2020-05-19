class Employee:
    def __init__(self):
        self._Ename = ""
        self._Esalary = 0
        self._Eage = 0
    def get_data(self):
        self._Ename=input("Enter Name: ")
        self._Esalary=int(input("Enter Salary: "))
        self._Eage=int(input("Enter Age: "))
    def put_data(self):
        print(self._Ename+" "+str(self._Esalary)+" "+str(self._Eage))
e = Employee()
print("Employee 1")
e.get_data()
e.put_data()
e1 = Employee()
print("Employee 2")
e1.get_data()
e1.put_data()
e2 = Employee()
print("Employee 3")
e2.get_data()
e2.put_data()
