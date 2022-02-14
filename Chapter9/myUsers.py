# you actually only need to import admin, since everything is encapsulated in the other classes 

# from user import User
from admin import Admin
# from privileges import Privileges


privList=["add a post", "remove a post", "ban a user"]

newAdmin = Admin("Joe", "Schmoe", "JoSo", "joSo3@ab.net", privList)

newAdmin.describe_admin()