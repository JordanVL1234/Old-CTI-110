###   JORDAN VICENTE-LACHAPELLE /-/ 11-26-23 /-/ CTI-110  -  P5HW - Math Quiz   ###
import random
import os
os.system('cls')

def NumRan():
    global Num1, Num2
    Num1 = round(random.random()*100)
    Num2 = round(random.random()*100)

def Menu():
    print("\nMAIN MENU")
    print("-----------------")
    print("1. Addind Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    MenuIn = input("\nPlease choose one of the menu options: ")
    return int(MenuIn)

def AddRan(Num1, Num2):
    print(f"  {Num1}")
    print(f"+ {Num2}")
    return(Num1+Num2)

def SubRan(Num1, Num2):
    if Num1 > Num2:
        print(f"  {Num1}")
        print(f"- {Num2}")
        return(Num1-Num2)
    else:
        print(f"  {Num2}")
        print(f"- {Num1}")
        return(Num2-Num1)

def Guess(NumOut):
    NumGuess = int(input("Enter answer.\n"))
    GuessCount = 1
    while NumGuess != NumOut:
        if NumGuess > NumOut:
            print(f"Sorry, guess is too high.")
        if NumGuess < NumOut:
            print(f"Sorry, guess is too low.")
        NumGuess = int(input("\nTry again: "))
        GuessCount += 1
    print("Congratulations!!!! Your answer is correct.")
    print(f"Number of guesses: {GuessCount}")

def main():
    print("Welcome to Math Quiz\n")
    MenuIn = Menu()
    while MenuIn != 3:
        if 0 < MenuIn and MenuIn < 3:
            NumRan()
            if MenuIn == 1:
                NumOut = AddRan(Num1, Num2)
                print()
            elif MenuIn == 2:
                NumOut = SubRan(Num1, Num2)
                print()
            Guess(NumOut)
        else:
            print("PLEASE SELECT A VALID OPTION!!!")
        MenuIn = Menu()
    print("Thank you for playing...")
    print("Bye!!")

if __name__ == '__main__':
    main()
