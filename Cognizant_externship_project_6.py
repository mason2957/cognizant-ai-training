# This project is meant to showcase input validation in a calculator program
def menu():
    while True:
        print("\nMENU:") ## menu to select the operation being performed
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit :(")

        choice = input("Enter your choice (1-5): ") ## enter the choice from the menu

        if choice == '5': ## if a user wants to leave it boots them before being forced to enter numbers
            print("Goodbye!")
            break ## breaks the loop

        if choice in ['1', '2', '3', '4']: ## pulls in the choice to be assessed by a new group of if statements
            try:
                n = int(input("\nPlease enter a number: ")) ## has the user input numbers
                x = int(input("Please enter a number: "))

            except ValueError: ## checks to make sure the inputs are the right kind of input
                print("Sorry, you must input a valid number!")
                continue ## brings the user back to the start if an error occurs

            else: ## if no error prints a lets get started message
                print(f'The numbers {n} and {x} are great choices!')

            finally: ## always prints a thankyou message
                print("Thank you for using this program!")

            if choice == '1': ## if choice is 1 it performs addition
                print(f"The sum of {n} and {x} is {n + x}.")

            elif choice == '2': ## if choice is 2 it performs subtraction
                print(f"The difference of {n} and {x} is {n - x}.")

            elif choice == '3': ## if Choice is 3 it performs multiplication
                print(f"The product of {n} and {x} is {n * x}.")

            elif choice == '4': ## if choice is 4 it performs division
                try:
                    print(f"The sum of {n} and {x} is {n / x}.")

                except ZeroDivisionError: ## checks to make sure the denominator is a non 0 number
                    print("Sorry, you cannot divide by zero!") ## pushes a friendly error message if it is


        else: ## makes sure the initial choice is between 1 and 5
            print("Invalid choice. Please enter 1-5.")

menu()