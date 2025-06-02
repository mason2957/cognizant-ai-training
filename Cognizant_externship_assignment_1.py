## Task 1

name = "Mason"
age = 25
height = 5.9

print("Hey how are you? My name is " + name + "! I am " + str(age) + " years old and " + str(height) + " feet tall.")
## I am printing a message combining the name,age, and height variables

## Task 2

num1 = 17
num2 = 23

print("The sum of 17 and 23 is ", num1 + num2) ## I am printing a message adding the two variables

print("After the subtraction of 17 and 23 you get ", num1 - num2) ## I am printing a message subtracting the two variables

print("After the multiplication of 17 and 23 you get ", num1 * num2) ## I am printing a message multiplying the two variables

print("After the division of 17 and 23 you get ", num1 / num2) ## I am printing a message dividing the two variables

## Task 3

x = int(input("Please enter a number: ")) ## Printing a message asking for an input and turning the input into a variable

if x > 0:
    print("This number is positive. Congrats!")
elif x < 0:
    print("This number is negative. Better luck next time!")
else:
    print("This number is zero. A perfect balance!")


