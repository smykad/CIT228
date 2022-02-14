class Restaurant:
    """ A simple attempt to model a Restaurant"""
    
    def __init__(self, name, cuisine):
        """Initialize restaurant name and cuisine type"""
        self.name = name
        self.cuisine = cuisine
        
    def describe_restaurant(self):
        """Simulate a description of the restaurant"""
        print(f"{self.name} serves {self.cuisine}")
        
    def open_restaurant(self):
        print(f"{self.name} is open")
        
    
myRestaurant = Restaurant("TGI Friday", "American")
myRestaurantA = Restaurant("Olive Garden", "Italian")
myRestaurantB = Restaurant("Hunan", "Chinese")
myRestaurantC = Restaurant("La Senorita", "Mexican")

restList = [myRestaurantA, myRestaurantB, myRestaurantC]

print('Exercise 9-1\n==================================================\n')
print(f"Restaurant = {myRestaurant.name}")
print(f"Cuisine = {myRestaurant.cuisine}")

myRestaurant.describe_restaurant()
myRestaurant.open_restaurant()

print('\nExercise 9-2\n==================================================\n')

for rest in restList:
    rest.describe_restaurant()
