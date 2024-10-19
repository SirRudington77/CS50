"""
implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
"""

def camelToSnake():
    # promp user for name
    camelcase = input("camelCase: ")
    separator = "_"
    snake_case = ""
    # checks to see if the string has an upper letter
    for case in camelcase:
        # replaces upper letter with underscore and lowercase of the letter
        if case.isupper():
            snake_case += separator + case.lower()
        # if there are no lower case, print as is
        else:
            snake_case += case
    # returns the value in snake case
    print(snake_case.strip())

camelToSnake()