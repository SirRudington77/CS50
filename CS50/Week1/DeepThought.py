"""
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
"""
def deepThoughts():
    # Get users input to question and converts input so that all input is lowercase
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").lower()
    if x == "42" or x == "forty-two" or x == "forty two":
    # outputs yes if answer is 42, forty-two or forty two 
        print("Yes")
    else:
    # outputs no if anything else
        print("no")


deepThoughts()




