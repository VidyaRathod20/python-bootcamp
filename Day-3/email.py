class Student:
    def __init__(self,name,roll,branch,address,email):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.address=address
        self.email=email
    def show(self):
        print("name is",self.name)
        print("roll no is",self.roll)
        print("branch",self.branch)
        print("address is",self.address)
        print("email is",self.email)
obj=Student("vidya",100,"CSE","itikyal","vidya@gmail.com")   #obj is creating
obj.show()
