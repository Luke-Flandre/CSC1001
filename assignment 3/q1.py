
class Flower:
    def __init__(self,name,petals,price):# Initialize the variables with appropriate values
        if type(name) != str:# If the type of the flower's name is not a string,it will tell the user.
            print('The input of the name is incorrect. A string is required')
        elif type(petals) != int:# If the type of the flower's petals is not a integer,it will tell the user.
            print('The input of the number of petals is incorrect. An integer is required')
        elif type(price) != float:# If the type of the flower's price is not a float,it will tell the user.
            print('The input of the price is incorrect. A float is required')
        self.name=name# Set the name of the flower
        self.petals=petals# Set the number of the petals
        self.price=price# Set the price of the flower
     
    def getValue(self):# Method to get the value of the flower
       info = {"name": self.name, "numPetal": self.petals, "price": self.price}
       return info

        
