from typing import Any


class Toy:
    def __init__(self,color,age) -> None:
        self.color=color
        self.age=age
        self.my_dict={
            "name":"Sanjeev",
            "age":25
            }     
        
    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 50
    
    def __call__(self):
        return('yesss??')
    
    def __getitem__(self,i):
        return self.my_dict[i]
    
action_figure=Toy('red',0)
print(action_figure.__str__())
print(str(action_figure))
print(action_figure.__len__())
print(len(action_figure))
print(action_figure['name'])