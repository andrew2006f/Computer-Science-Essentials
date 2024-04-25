fileName = "textfile.tt"

def textInFile(content):
    try:
        with open(fileName, 'a') as file:
            content = content + "\n"
            file.write(content)
            print("connect added!")
            file.close()
    except:
        print("An error has occured")

def readFromFile():
    try:
        with open(fileName, 'r') as file:
            content = file.read()
            print(content)
            file.close()
    except:
        print("An error has occured")

while True:
    print("Pick an option.")
    print("1 - Send data   2 - read data   3 - exit program")
    choice = input("-->")
    if choice == "1":
        print("Write the data you would like to send")
        content = input("->")
        textInFile(content)
        print("Text added to file")

    elif choice == "2":
        print("Reading text file")
        readFromFile()

    elif choice == "3":
        break
print("Bye")
