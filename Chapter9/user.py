class User:
    def __init__(self,firstName,lastName,userName,email):
        self.firstName=firstName
        self.lastName=lastName
        self.userName=userName
        self.email=email

    def describe_user(self):
        print(f"{self.firstName} {self.lastName}'s username is {self.userName} and their email is {self.email}")