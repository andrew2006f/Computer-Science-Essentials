import random

response = ""

print("Welcome to the Magic 8 Ball!")
print("You have to ask a question, and the 8 ball will give you a random response!")
while True:
    input("Ask a yes/no question...")

    response = random.randint(1,8)

    if response == 1:
        response = "Yes"
    if response == 2:
        response = "No"
    if response == 3:
        response = "I don't know"
    if response == 4:
        response = "I don't care"
    if response == 5:
        response = "Sure"
    if response == 6:
        response = "If you want"
    if response == 7:
        response = "Repeat that"
    if response == 8:
        response = "Maybe"

    print(response)
