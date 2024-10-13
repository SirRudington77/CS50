def energy():
    # User input of mass
    m = int(input("Type mass number: "))
    # Take user input and return value of E
    # E= mc^2. c = 300000000
    c = 300000000
    e = m * c ** 2
    print(e)

energy()
