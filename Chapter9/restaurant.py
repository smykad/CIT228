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