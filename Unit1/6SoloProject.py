print("Welcome to the exponent calculator")
print("This Calculator calculates any exponent you want.")
num1 = input("Enter your base")
num2 = input("Enter your exponent")
answer = (int(num1) ** int(num2))
print(answer)

if answer > 50:
    print("That's a large number")
elif answer < 50:
    print("That's a small number")
else:
    print("ERROR")

