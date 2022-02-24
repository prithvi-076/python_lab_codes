import datetime
hr = datetime.datetime.now()
class Restaurant:
    def __init__(self, res_name, cuisine):
        self.res_name = res_name
        self.cuisine = cuisine
    def describe_restaurant():
        print(f"Welcome to {self.res_name}")
        print(self.cuisine)
    def open_restauant(self):
        if(hr >= 11 and hr <= 23):
            print("Restaurant Open")
        else:
            print("Restaurant Closed")
name = input("Enter the Restaurant name: ")
cuisine_type = input("Enter the Cuisine: ")
obj = Restaurant(name, cuisine_type)
obj.describe_restaurant()
obj.open_restaurant()