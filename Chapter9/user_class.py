class User:
    def __init__(self, firstName, lastName, userName, password, email):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.password = password
        self.email = email
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"{self.firstName.title()} {self.lastName.title()} has a username of {self.userName},\n\
a password of {self.password} and an email address of {self.email}")
        
    def greet_user(self):
        print(f"Welcome back {self.firstName.title()}")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
        if self.login_attempts > 5:
            print(f"{self.firstName} you have exceeded the number of login attempts")
            self.reset_login_attempts()
        else:
            print(f"{self.firstName} has tried to login {self.login_attempts}")
            
            
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"The number of login attempts has been reset to: {self.login_attempts}")
        print("Your account has been locked for 30 minutes, please try back later or call tech support for help!")
        
myUserA = User("george", "Jetson", "georgejetson", "astro123", "george@jetson.net")
myUserB = User("wilma", "flintstone", "flinty", "pebbles", "wilma@flint.net")
myUserC = User("betty", "rubble", "bets", "bambam", "bets@rub.net")
myUserD = User("flo", "schmoe", "flow", "eieiflo", "flo@schmoe.net")

index = 0

myUserList = [myUserA, myUserB, myUserC]

print('Exercise 9-3\n==================================================\n')

for user in myUserList:
    user.greet_user()
    user.describe_user()

print('Exercise 9-5\n==================================================\n')

myUserD.describe_user()
while index < 6:
    myUserD.increment_login_attempts()
    index +=1

