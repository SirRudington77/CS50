def main():
    # user input
    x = str(convert(input("Type something: ")))
    print (x)

def convert(y):
    # replaces user input :) or :( with emoji    
    y = y.replace(":(", "🙁").replace(":)", "🙂")
    return y

main()