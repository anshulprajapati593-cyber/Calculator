import os

print ("Hello Human!! Welcome to the calculator")

history = []

def calculator():

    global history

    while True:

        os.system('cls' if os.name == 'nt' else 'clear')

        print("What do you wish to do?: ")
        print("1. Open calculation history  ----  (1)")
        print("2. Make Calculations         ----  (2)")
        options = input("Enter the corrsponding number of the function you want me to carry out: ")

        if options == "1":

            if not history:
                print("\nYour History is empty.")

            else:
                for numbers, elements in enumerate(history, start=1):
                    print(f"{numbers}. {elements}")

            input("\nPress Enter to return to the main menu.")

        elif options == "2":
            print("\nUse: (*) for Multiplication and (/) for Division.")
            equation = input("Enetr the full calculation: ")

            try:
                result = eval(equation)

                print(f"Result: {result}")

                history.append(f"{equation} = {result}")

            except ValueError:
                print("Error: You cannot Divide by Zero(0).")

            except Exception:
                print("Error: Invalid Equation. ")

            input("\nPress Enter to continue.")

calculator()
