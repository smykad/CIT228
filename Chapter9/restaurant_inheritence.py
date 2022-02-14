class Restaurant:
    """ A simple attempt to model a Restaurant"""
    
    def __init__(self, name, cuisine, numberServed = 0):
        """Initialize restaurant name and cuisine type"""
        self.name = name
        self.cuisine = cuisine
        self.numberServed = numberServed
        
    def describe_restaurant(self):
        """Simulate a description of the restaurant"""
        print(f"{self.name} serves {self.cuisine}")
        
    def open_restaurant(self):
        print(f"{self.name} is open")
        
    def set_number_served(self, numberServed):
        self.numberServed = numberServed
        print(f"How many customers have been served today? {self.numberServed}")
        print(f"The number of customers served is currently {self.numberServed}\n")
        
    def increment_number_served(self, numberServed):
        print(f"How many additional customers have been served? {numberServed}\n")
        self.numberServed += numberServed
        print(f"The number of customers served this business day = {self.numberServed}")
        

class IceCreamStand(Restaurant):
    
    def __innit__(self, name, cuisine, numberServed, flavors):
        super().__innit__(name, cuisine, numberServed)
        self.flavors = flavors

    def set_flavors(self, flavors):
        self.flavors = flavors

    def display_flavors(self):
        print(f"The flavors available at {self.name} are", end=": ")
        i = len(self.flavors)
        index = 0
        for flavor in self.flavors:
            if index < i-1:
                print(flavor, end=", ")
                index += 1
            else:
                print(flavor)
            
        


myFlavors = ['Vanilla', 'Chocolate', 'Stawberry']
myScream = IceCreamStand("Dairy queen", "American")

myScream.set_flavors(myFlavors)
myScream.display_flavors()

