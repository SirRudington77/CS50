"""
In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
"""
# create a convert function that is called by main
def main():
    # Prompt user for a time. 24-hour format #:## or ##:##
    x = input("What time is it?: ")

    # Output either breakfast, lunch or dinner. 
    if 6.0 <= convert(x) <= 10.0:
        print ("breakfast time")
    elif 12.0 <= convert(x) <= 14.0:
        print("lunch time")
    elif 18.0 <= convert(x) <= 21.0:
        print("dinner time")
    # if not a meal, no output
    else:
        pass

def convert(x):
    hour, minute = x.split(":")
    # converts string to a float. 7:30 or 07:30 converts and returns 7.5
    hour = float(hour)
    minute = float(minute)
    decimalConversion = float(hour + (minute / 60))
    return round(decimalConversion)


if __name__ == "__main__":
    main()