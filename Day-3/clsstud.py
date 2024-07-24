'class Student:
    #static 
    branch="CSE"
    def __init__(self,name,roll,address,email):
        self.name=name
        self.roll=roll
        
        self.address=address
        self.email=email
    def show(self):
        print("name is",self.name)
        print("roll no is",self.roll)
        print("branch",Student.branch)#creating with classname
        print("address is",self.address)
        print("email is",self.email)
obj=Student("vidya",100,"itikyal","vidya@gmail.com")   #obj is creating
obj.show()
