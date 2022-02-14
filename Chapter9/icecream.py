from restaurant import Restaurant

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