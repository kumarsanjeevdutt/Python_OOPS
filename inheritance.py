class User:
    
    def __init__(self,email) -> None:
        self.email=email
    
    
    def signin(self):
        print(f"{self.email} Logged in Successfully")
        


class Wizard(User):
    def __init__(self,name,power,email):
        User.__init__(self,email)
        self.name=name
        self.power=power
        
    def attack(self):
        print(f'{self.name} is attacking with the power of {self.power}')


class Archer(User):
    def __init__(self,name,arrow_type,email):
        super().__init__(email)
        self.name=name
        self.arrow_type=arrow_type
        
    def attack(self):
        print(f'{self.name} is attacking with the power of {self.arrow_type} arrow')


wizard1=Wizard('Merlin',"Dark Magic","merlin@gmail.com")
print(dir(wizard1))#introspection ------> ability to determine the type of an object during runtime
print(isinstance(wizard1,Wizard))
archer1=Archer('Robin','Poison',"Robin@yoho.com")
print(wizard1.signin())
wizard1.attack()
print(wizard1.email)
archer1.attack()