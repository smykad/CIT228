from user import User
from privileges import Privileges

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