#INHERITANCE
'''class Vehicle:
    def brake():
        print("brake adhists movement of a vehicle")
    def clutch():
        print("this is clutch")
    def accelerator():
        print("increases speed")
    def tyre():
        print("this is tyre")
class bike(Vehicle):
    def handle():
        print("turns the bike")
    def horn():
        print("makes sound")
bobj=bike
bobj.handle()
bobj.horn()
bobj.clutch()
bobj.tyre()
vobj=Vehicle'''

#MUTIPLE INHERITANCE
#ABSTRACTION
from abc import ABC
class Mobile(ABC):
    def storage():#abstract methood
        pass
    def calling():#non abstract method
        print("hey iam calling")
class Samsung(Mobile):
    def storage():
        print("samsung has 128gb storage")
    def camera():#non abstract
        print("50mp")
class iphone(Mobile):
    def storage():
        print("iphone has 258gb storage")
class vivo(Mobile):
    def storage():
        print("vivo has 64gb")
samobj=Samsung
samobj.storage() #displays only samsung storage
samobj.camera()
iphoneobj=iphone
iphoneobj.storage()
vivoobj=vivo
vivoobj.storage()
vivo.calling()




