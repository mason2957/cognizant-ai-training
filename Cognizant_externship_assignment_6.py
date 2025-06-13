# Creating fault-tolerant code
## Task 1 - Understanding Python exceptions
try: ## creates the initial input and operation
    n = int(input("Please enter a number: "))
    print(f'The answer is: {100 / n}!')

except ValueError: ## creates a nice error message if the user inputs something non-numeric
    print("Sorry that's not a valid number.")

except ZeroDivisionError: ## creates a nice error message incase the user trys to divide 100 by 0
    print("Sorry you cant divide by zero.")

## Task 2 - Types of Exceptions
## Trying to pull from an index that is out of range
my_list = ['apple', 'orange', 'banana', 'cherry'] ## creating the list

print(my_list)

try:
    print(my_list[6]) ## trying to print a non-existent index

except IndexError: ## catching the error with a friendlier message
    print("Sorry index out of range, choose an index between 0 and 3.")

## Trying to access a non-existent key in the dictionary
my_dict = { ## creating the dictionary
    'name': 'mason',
    'age': 25,
    'major' : 'IT',
    'pet' : 'cat'
}

print(my_dict)

try: ## trying to access a key that doesn't exist in the dictionary
    print(my_dict['book'])

except KeyError: ## catching the error and printing a more friendly message
    print("Sorry that key is not in the dictionary.")

## trying to add a string and an integer
try:
    print("hello" + 25) ## trying to add a string and integer which aren't the same types

except TypeError: ## returning a friendlier message
    print("Sorry that's not a valid number, you can't add a string and integer.")

## Task 3 - using try... except... else... finally
try:
    n = int(input("\nPlease enter a number to be divided: "))
    x = int(input("Please enter a number to divide the number by: "))

    result = (n / x)

except ZeroDivisionError:
    print("Sorry, you can't divide by zero!")

except TypeError:
    print("Sorry, you must input a number!")

except ValueError:
    print("Sorry, you must input a number!")

else:
    print(result)

finally:
    print("Thank you for using this program!")

