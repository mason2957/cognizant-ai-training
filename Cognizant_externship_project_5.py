# Creating a menu of recursive functions
def factorial(n): ## creating the factorial function
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n): ## creating the fibonacci function
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def menu():
    while True:
        print("\nMENU:")
        print("1. Calculate the factorial of a number")
        print("2. Find the nth Fibonacci number")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            n = int(input("Enter a non-negative integer: "))
            if n < 0:
                print("Please enter a non-negative number.")
            else:
                print(f"Factorial of {n} is {factorial(n)}")

        elif choice == '2':
            n = int(input("Enter the position (n) in the Fibonacci sequence: "))
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                print(f"The {n}th Fibonacci number is {fibonacci(n)}")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-3.")

menu()