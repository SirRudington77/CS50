def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # accept str formatted as $##.##. Remove the $ and return amount as a float. Should return ##.#
    d = float(d.strip("$"))
    return d


def percent_to_float(p):
    # accept a st formatted as ##%, remove the trailing %, return the percentage as a float. #.##
    p = float(p.strip("%")) / 100
    return p


main()
