# Creating Functions in Python
## Task 1 - Creat two functions, one that greats a user and another that takes two numbers as parameters and adds them
def add(a, b): ## creates a function to add two numbers together
    return a + b

def greet_user(name, a, b): ## creates the function to great a specific user and incorporates the add function
    print(f'Hello, {name}! The sum of {a} + {b} is {add(a, b)}!')

greet_user('Michael', 7, 4) ## function testing

## Task 2 - create a function that uses default parameters
def describe_pet(pet_name, animal_type = "dog"):
    print(f'I have a {animal_type} named {pet_name}!')

describe_pet(input('What is the name of your pet: '), input('What type of animal is your pet: '))
describe_pet('Charlie')

## Task 3 - Functions with variable arguments
def make_sandwich(*args): ## define function with variable arguments
    ingredients = ", ".join(args) ## creating a way to join the arguments into one string
    return f'Make a sandwich with: {ingredients}.' ## the output

print(make_sandwich('Turkey', 'Wheat', 'Mustard'))

## Task 4 - Understanding Recursion
def factorial(n): ## creating the factorial function
    if n == 1:
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

def fact_and_fib(n): ## creating a function that combines the two
    return f'The factorial of {n} is {factorial(n)}. The {n}th Fibonacci number is {fibonacci(n)}.'

print(fact_and_fib(10))
