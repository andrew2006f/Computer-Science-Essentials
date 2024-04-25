#Car Maker 
#This code demonstrates how Object-Oriented programming (OOP) works
#In this case, you are building cars. The cars are the object
#The car(object) has properties (doors, color, wheel size, horsepower, etc.)
#Since each car is a different object, we use the code below to create as many cars as we want

class Car:
    def __init__(self, numOfDoors, color, horsePower, rims, tint):
        #Update this code to include your two new properties from below
        self.numOfDoors = numOfDoors
        self.color = color
        self.horsePower = horsePower
        self.rims = rims
        self.tint = tint
        print("Car Successfully created!")

print("Welcome to the custom car maker app")

#Add two more properties for a car object below. 
doors = input("How many doors would you like your car to have? ")
color = input("What color would you like your car to be? ")
hp = input("How much horsepower would you like your car to have? ")
rims = input("What color rims would you like your car to have?")
tint = input("What % tint would you like?")
#update this code below to show your two new properties from above
c1 = Car(doors, color, hp, rims, tint)
print("Your car will have", c1.numOfDoors, " Doors.")
print("It will be the color", c1.color)
print("and will have", c1.horsePower, " horsepower.")
print("and it will have", c1.rims, " rims.")
print("and it will have", c1.tint, "% tint")
