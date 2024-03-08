print("Welcome to the Did I Fail? Calculator.")
print("This Calculator will tell whether or not you failed.")
num1 = input("How many points was the grade out of?")
num2 = input("What did you score?")
grade = int(num2)/int(num1) * 100
print(grade)
if grade > 59.5:
    print("You passed!")
else:
    print("You failed.")
