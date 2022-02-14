class Restaurant:
    """ A simple attempt to model a Restaurant"""
    
    def __init__(self, name, cuisine):
        """Initialize restaurant name and cuisine type"""
        self.name = name
        self.cuisine = cuisine
        self.numberServed = 0
        
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
        

print('Exercise 9-4\n==================================================\n')

myRestaurantA = Restaurant("Outback Steakhouse", "Australian")

myRestaurantA.open_restaurant()
myRestaurantA.describe_restaurant()

# processing intitial number served #
print(f"\nThe starting number of customers was: {myRestaurantA.numberServed}\n")

# changing the numberServed attribute to 200 #
myRestaurantA.numberServed = 200
print(f"The number of customers served has been changed to: {myRestaurantA.numberServed}\n")

# changing the numberServed using the set_number_served method #
myRestaurantA.set_number_served(300)

myRestaurantA.increment_number_served(45)

