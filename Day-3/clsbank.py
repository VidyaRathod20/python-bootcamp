'''class Student:
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
obj=Student("keerthi",100,"itikyal","keerthi@gmail.com")   #obj is creating
obj.show()'''


class Bank:
    ifsc=15790
    def __init__(self,name,accountno,address,mobileno):
        self.name=name
        self.accountno=accountno
        self.address=address
        self.mobileno=mobileno
    def display(self):
        print("name of account holder is",self.name)
        print("account number is",self.accountno)
        print("Address is",self.address)
        print("mobile number is",self.mobileno)
        print("ifsc code is",Bank.ifsc)
b=Bank("keerthi",1901000234,"itikyal",6301222627)
b.display()'''
