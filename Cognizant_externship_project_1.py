## this is a program to check voter eligibility
age = int(input("How old are you? ")) ## here we ask the user to enter their age and convert it to an integer

if age >= 18:
    print("Congratulations! You are able to vote!") ## this assesses if the age variable is 18 or above
else:
    print("Sorry, you are not able to vote yet! Only a few years left though!") ## this assesses if the age variable is under 18
