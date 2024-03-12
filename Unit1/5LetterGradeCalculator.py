print("Welcome to the Letter Grade Calculator.")
print("This Calculator will tell you what grade you got.")
num1 = input("How many points was the grade out of?")
num2 = input("What did you score?")
grade = int(num2)/int(num1) * 100
print(grade)
if grade > 89.5:
    print("You got an A!")
    print("You passed")
elif grade > 79.5:
     print("You got an B!")
     print("You passed")
elif grade > 69.5:
     print("You got a C!")
     print("You passed")
elif grade > 59.5:
     print("You got a D!")
     print("You passed")
elif grade < 59.5:
     print("You got an F!")
     print("You failed")
else:
     print("Error")
