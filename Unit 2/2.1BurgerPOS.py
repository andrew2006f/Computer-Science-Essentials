#BROWNTOWN BURGER JOINT POINT OF SALE SOFTWARE
#VERSION 1.21 LAST REVISION DATE 3/11/2024


#VARIABLES
orderComplete = False
totalCost = 0
tax = 0.06
orderSummary = ""

#WELCOME THE USER TO THE POINT OF SALE(POS)
print("Welcome to the Browntown Burger Joint, voted 2nd best Burger in Browntown")
print("We sell burgers, drinks, and sides.")

#ASK THEM FOR THEIR NAME AND STORE IT IN name
name = input("Can I have your name please?  ")
print()
print("Thanks " + name)
print()
print()


#POINT OF SALE LOOP
while orderComplete == False:
    #STAY IN THIS LOOP UNTIL THEY SELECT "COMPLETE ORDER"
    print()
    print ("What would you like to order: Burgers, Sides, Drinks, Complete Order.")
    menu = input("-> ")
    
    
    if menu == "Burgers":
        #IF THEY WANT TO ADD A BURGER:
        print("We offer the following burgers:")
        print("1: Hamburger $5.50")
        print("2: Cheesebuger $6.00")
        print("3: Western burger (Cheese, onion, western sauce) $6.75")
        print("4: Bacon Cheeseburger $6.50")
        burgerChoice = input("What would you like (input a number 1-4): ")
        #BURGER 1: HAMBURGER
        if burgerChoice == "1":
            totalCost = totalCost + 5.50
            print("You added Hamburger to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Hamburger "

        #BURGER 2: CHEESEBURGER
        elif burgerChoice == "2":
            totalCost = totalCost + 6.00
            print("You added Cheeseburger to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Cheeseburger "

        #BURGER 3: WESTERN BURGER
        elif burgerChoice == "3":
            totalCost = totalCost+ 6.75
            print("You added Western Burger to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Western Burger "
        
        #BURGER 4: BACON CHEESEBURGER
        elif burgerChoice == "4":
            totalCost = totalCost+ 6.50
            print("You added Bacon Cheeseburger to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Bacon Cheeseburger "

            
        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELECTION
        else:
            print("please make a valid choice")
        
    elif menu == "Sides":
        print("We offer the following sides:")
        print("1: French Fries $3.00")
        print("2: Mashed Potatoes $3.50")
        print("3: Tater Tots $4.00")
        sideChoice = input("What would you like (input a number 1-3): ")

        #SIDE 1: FRIES
        if sideChoice == "1":
            totalCost = totalCost + 3.00
            print("You added French Fries to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "French Fries "
        #SIDE 2: MASHED POTATOES
        if sideChoice == "2":
            totalCost = totalCost + 3.50
            print("You added Mashed Potatoes to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Mashed Potatoes "
        #SIDE 3: TATER TOTS
        if sideChoice == "3":
            totalCost = totalCost + 4.00
            print("You added Tater Tots to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Tater Tots "
    
    elif menu == "Drinks":
        print("We offer the following drinks:")
        print("1: Dr. Pepper $2.00")
        print("2: Coke $2.00")
        print("3: Mountain Dew $2.00")
        drinkChoice = input("What would you like (input a number 1-3): ")
        #DRINK 1: DR. PEPPER
        if drinkChoice == "1":
            totalCost = totalCost + 2.00
            print("You added Dr. Pepper to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Dr. Pepper "
        #DRINK 2: COKE
        if drinkChoice == "2":
            totalCost = totalCost + 2.00
            print("You added Coke to your order")
            print("Your total cost so far: $", totalCost)
            orderSummary = orderSummary + "Coke "
        #DRINK 3: MOUNTAIN DEW
        if drinkChoice == "3":
            totalCost = totalCost + 2.00
            print("You added Mountain Dew to your order")
            print("Your total cost so far: $", totalCost) 
            orderSummary = orderSummary + "Mountain Dew " 
    
    elif menu == "Complete Order":
        #IF THEY SELECT COMPLETE ORDER, SET THE ORDERCOMPLETE TO TRUE
        orderComplete = True
        print("Your order has been finalized!")

        #GIVE THEM THEIR TOTALS
        print("order finished")
        print("You have ordered", orderSummary)
        print("Subtotal: $", totalCost)
        totalTax = float(totalCost) * tax
        print("Total Tax: $", totalTax)
        print("Grand Total: $", totalCost + totalTax)
        #Finish this section to give you a grand total as well as print your complete order
 
        
    else:
        print("Sorry, not a valid choice, please start over...")

#THE USER ONLY GETS HERE IF THEY FINISH THEIR ORDER
print("Thank you for eating with us!")
