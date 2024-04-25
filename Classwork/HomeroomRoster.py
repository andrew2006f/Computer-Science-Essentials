#Homeroom Roster Program
#This program is designed to allow a teacher to:
#1) See students in homeroom
#2) Add students/remove to homeroom
#3) See basic info about students

class Student:
    def __init__(self, name, grade, age, ID, address, locker_number):
        self.name = name
        self.grade = grade
        self.age = age
        self.ID = ID
        self.address = address
        self.locker_name = locker_number

roster = []

#Functions
def add_to_homeroom():
    #Create a new student object with the following properties:
    #name, grade, ID, address, age, lock_number
    
    #Name
    print("Creating new student:")
    name = input("What is their name?")

    #Grade
    grade = input("What is their grade?")

    #Age
    age = input("What is their age?")

    #ID
    ID = input("What is their ID?")

    #Address
    address = input("What is their address?")

    #Lock_Number
    locker_name = input("What is their locker number?")

    #Create the student object using the variables created above
    #name, grade, ID, address, age, locker_name 
    new_student = Student(name, grade, ID, address, age, locker_name)
    roster.append(new_student)
    print("Created a student with the details below:")
    print("Name:", new_student.name)
    print("Grade:", new_student.grade)
    print("ID:", new_student.ID)
    print("Address:", new_student.address)
    print("Age:", new_student.age)
    print("Locker Number:", new_student.locker_name)

def get_number_of_students():
    length = len(roster)
    return length
def search_list_for_student(search_name):
    for counter in roster:
        if search_name == counter.name:
            print("This student is on the list")
            return
    print("This student is not on the list")

def get_student_address(search_name):
    print("Searching list for student's address")
    for counter in roster:
        if counter.name == search_name:
            print(counter.address)


def get_student_basic_info(search_name):
    print("Getting information about this student")
    for counter in roster:
        if counter.name == search_name:
            print("Grade: ", counter.grade)
            print("ID: ", counter.ID)
            print("Address: ", get_student_address(search_name))
            print("Age: ", counter.age)
            print("Locker Number: ", counter.locker_number)


def list_homeroom_students():
    for counter in roster:
        print(counter.name) 

while True:
    print("What would you like to do:")
    print("1: View Homeroom  Roster")
    print("2: Remove student from homeroom")
    print("3: Add student to homeroom")
    print("4: See number of students in Homeroom")
    print("5: See basic information")
    print("6: See if a student is on the homeroom list")
    print("7: Exit Program")
    try:
        choice = int(input("->"))
        if choice == 1:
            #See list of students
            print("Now Showing the List of Homeroom Students")
            list_homeroom_students()
        elif choice == 2:
            #Add students to homeroom
            add_to_homeroom()
        elif choice == 3:
            #Remove student from homeroom
            pass
        elif choice == 4:
            #See number of students in Homeroom
            print("Getting number of Homeroom Students")
            print(get_number_of_students())
        elif choice == 5:
            #See basic information
            pass
        elif choice == 6:
            #See if a student is on the homeroom list
            search_name = input("What student do you want to search?")
            search_list_for_student(search_name)
        elif choice == 7:
            #Exit program
            break
        else:
            print("An error has occured")
    except:
        print("Please use a valid number")

print("Thanks for using the homeroom software")
