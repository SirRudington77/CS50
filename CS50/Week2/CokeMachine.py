# Not passing the check. Need to troubleshoot for the correct results
def cokeMachine():
    # Set values
    coke = 50
    coins = [25, 10, 5]
    print("Amount due: " + str(coke))

    # creating a loop to continuously ask user for coins until amout is 0
    while coke > 0:
        # users input
        usersChange = int(input("Insert coin: "))
        # check if user input matches list
        if usersChange in coins:
            # subtract amount user put in
            coke -= usersChange
            # updates amout 
            if coke > 0:
                print("Amount due: " + str(coke))
            # if over paid
            elif coke < 0:
                print("Amount owed: " + str(abs(coke)))
            # amount is paid off
            else:
                print("Amount due: 0")
        # invalid inputs
        else:
            print("Please enter a correct amount!")


cokeMachine()