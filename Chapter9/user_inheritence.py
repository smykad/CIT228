class User:
    def __init__(self,firstName,lastName,userName,email):
        self.firstName=firstName
        self.lastName=lastName
        self.userName=userName
        self.email=email

    def describe_user(self):
        print(f"{self.firstName} {self.lastName}'s username is {self.userName} and their email is {self.email}")           

class Admin(User):
    def __init__(self,firstName,lastName,userName,email, permissions):
        super().__init__(firstName,lastName,userName,email)
        self.permissions=Privileges(permissions)

    def describe_admin(self): 
        print("========================================")
        print(f"Name: {self.firstName} {self.lastName}")  
        print(f"Username: {self.userName}")  
        print(f"E-mail: {self.email}")  
        self.permissions.show_privileges()   
        print("========================================")
  
class Privileges:
    def __init__(self,permissions):
        self.permissions=permissions

    def show_privileges(self):
        print(f"The being has the following powers:")
        for p in self.permissions:
                print(p.title())

privList=["add a post", "remove a post", "ban a user"]

newAdmin = Admin("Joe", "Schmoe", "JoSo", "joSo3@ab.net", privList)

newAdmin.describe_admin()
