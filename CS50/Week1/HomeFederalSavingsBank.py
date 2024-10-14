"""
In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
"""
def greetingWorld():
    # prompt user for a greeting
    greeting = input("How do you normally greet people?: ").lower().strip()

    # if greeting starts with 'hello' = $0
    if greeting.startswith("hello"):
        print("$0")
    # if greeting starts with 'h' and not hello = $20
    elif greeting.startswith("h") and greeting != "hello":
        print("$20")
    # Anything else = $100
    else:
        print("$100")


greetingWorld()

