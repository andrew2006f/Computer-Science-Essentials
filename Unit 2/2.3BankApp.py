#1st National Bank of Browntown Online Banking Application


class Customer():
    #This is an OBJECT. It has properties of Withdraw, Deposit, BalanceCheck
    def __init__ (self, name, balance = 100.00):#This gives the user 100 bucks to start
        self.name = name
        self.balance = balance
        print("Account made for", name, " Current Balance: $", balance)

    def withdraw(self,amount):#This is the withdraw function
        self.balance = self.balance - amount
        return self.balance

    def deposit(self,amount):#This is the deposit function
        self.balance = self.balance - amount
        return self.balance

    #Add the ability to check balance
    def BalanceCheck(self, amount):#This function allows the user to check their balance
       return self.balance

print("Welcome to the 1st National Bank of Browntown App")
print("All new customers get $100 deposited into their account for signing up!")
print()

name = input("Let's Get Started! What is your name: ")
customer = Customer(name)#Gives the user a name
while True:
    print("What would you like to do: (1) Withdraw   (2) Deposit   (3) Check Balance    (4) Log out")
    choice = input("->")

    #Withdraw
    if choice == "1":#Withdraw choice
        print("How much are you withdrawing")
        amount = float(input("->"))
        balance = customer.balance - amount
        customer.withdraw(amount)
        print("You have withdrawn ", amount)
        print("You now have... ", balance) 

    #Add the ability to deposit
    elif choice == "2":#Deposit choice
       print("How much would you like to deposit?")
       amount = float(input("+>"))
       balance = customer.balance + amount
       customer.deposit(amount)
       print("You have deposited", amount)
       print("You now have... ", balance) 

    elif choice == "3":#Check Balance choice
        balance = customer.balance
        print("Your balance is $", balance)
    elif choice == "4":#Log out choice
        print("You have successfully logged out")
        break
    else:
        print("You have entered an illegal value, please try again.")
