class Privileges:
    def __init__(self,permissions):
        self.permissions=permissions

    def show_privileges(self):
        print(f"The being has the following powers:")
        for p in self.permissions:
                print(p.title())