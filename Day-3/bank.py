class Bank:
    def __init__(self,name,accountno,address,mobileno):
        self.name=name
        self.accountno=accountno
        self.address=address
        self.mobileno=mobileno
    def dispaly(self):
        print("name of account holder is",self.name)
        print("account number is",self.accountno)
        print("Address is",self.address)
        print("mobile number is",self.mobileno)
b=Bank("vidya")
