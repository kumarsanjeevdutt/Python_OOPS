#Class is nothing but a blueprint to define something 
# __init__ is  a constructor method which is also called the Magic Methods or Dunder methods
# self here points to the PlayerCharacter so taht any object that is created the self points to it 


class PlayerCharacter:
    
    Membership=True  #Class Object Attributes these are not same the class attributes because these are not dynamic but it is a constant attribute of the class andis available for all the objects instanciated 
    def __init__(self,name,age):
        if (self.Membership):#This can also be accessed by saying PlayerCharacter.Membership
            self.name=name #Attributes
            self.age=age

    def run(self):
        return f"{self.name} is {self.age} years old"
       # return f"{PlayerCharacter.name} is {PlayerCharacter.age} years old"  #here i cannot use the PlayerCharacter.name it will throw an error like ""AttributeError: type object 'PlayerCharacter' has no attribute 'name'"
          
    @classmethod
    def adding_things(cls,num1,num2):   #we use cls here instead of self it is same like slef but teh first arg the classmethod would take is the cls
        # here we can actually use the cls to instanciate a object here
        # return cls("Lovely",num1+num2)
        return num1+num2
    
    #the staticmethod is same as the class method except for that we dont have access to the cls parameter here instead we just performa  method like adding up for example
    @staticmethod
    def adding_things2(num1,num2):
        return num1+num2


player1=PlayerCharacter("Sanjeev",22)
player2=PlayerCharacter("Jaydutt",20)
player3=PlayerCharacter.adding_things(7,9)

print(player1.name)
print(player1.run())
print(player2.name)
print(player2.run())

# print("@classmethod",player1.adding_things(2,8))
print("@classmethod",PlayerCharacter.adding_things(2,8)) #we can also use the direct class name without actually instanciating the class 

# print(player3.name,player3.age)