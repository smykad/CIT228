class Employee:
    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
    
    def give_raise(self, payraise=5000):
        self.salary += payraise

