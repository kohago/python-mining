class Person:
    #所持金
    deposit = 10

    def __init__(self):
        self.deposit = 0

    def normal_method(self,money):
        return self.deposit + money

    @classmethod
    def class_method(cls,money):
        return cls.deposit + 2 * money

    @staticmethod
    def static_method(money):
        return Person.deposit + money * 3

person = Person()
# __init__ will be executed automiclly => deposit is 0
#person.__init__()
print(person.deposit) # => 0
#when called from instance, self will be the instance
print(person.normal_method(10)) #=> 10
#when called from instance,cls will be the class of the instance
print(person.class_method(10)) # =>30
#no self ,no cls,just the parameters
print(person.static_method(10)) # =>40
