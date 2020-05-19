class Teacher:
    def __init__(self):
        self._Stu_Name = ""
        self._Subject = ""
        self._Basic = 0
        self._DA = 0
        self._HRA = 0
        self._Salary = 0
    def get_data(self):
        self._Stu_Name = input("Enter Name:")
        self._Subject = input("Enter Subject")
        self._Basic = int(input("Enter Salary"))
    def put_data(self): 
        self._DA = (5*self._Basic)//100
        self._HRA = (10*self._Basic)//100
        self._Salary = self._DA+self._HRA+self._Basic
        print(self._Salary)
tch = Teacher()
tch.get_data()
tch.put_data()
