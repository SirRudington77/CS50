# #prompt user to input string
# x = str(input("Please type something: "))
# x = x.replace(' ', '...')

# #output the same with '...' replacing space
# print(x)

# takeing the code and creating it into a function
def threeDots():
    x = str(input("Please type in something: ")).replace(' ', '...')
    print(x)

threeDots()