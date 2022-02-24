class Robot:
    def __init__(self,name):
        self.name=name      
    def display(self):
        print(f"Robot says hello to {self.name}")
name=input("Enter your name: ")
obj=Robot(name)
obj.display()