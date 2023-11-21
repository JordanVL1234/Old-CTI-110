###   JORDAN VICENTE-LACHAPELLE / ALLISON QUINN / JOSH ADAMS   /-/   11/21/23   ###

import os
os.system('cls')

def ConvertCM(inches):
    centimeters = float(inches) * 2.54
    return centimeters

def ConvertM(centimeters):
    meters = centimeters / 100
    return meters

def Output(centimeters, meters):
    print(f"\n{inches} inches is {centimeters} centimeters")
    print(f"{centimeters} is {meters} meters")

def main():
    global inches
    inches = input("Enter a value in inches: ")
    while str(inches) != "end":
        centimeters = ConvertCM(inches)
        meters = ConvertM(centimeters)
        Output(centimeters, meters)
        print("\n\n")
        inches = input("Enter a value in inches: ")

if __name__ == '__main__':
    main()
