class A:
    __amount = 45

    def __info(self):
        print("I am in Class A")

    def hello(self):
        print ("Amount is ",A.__amount)    # private variable within the class

a = A()
a.hello()           #within the class - the variable is accessible
#a.__info()          # will not work like this as there is there is no attribute. To access private variables syntax is: _class-name__private-attribute.
a._A__info()         #correct way to access the private method - showing class then method
print (a._A__amount)  #correct way to access the private private - showing class then method
