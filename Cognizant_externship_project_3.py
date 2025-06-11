# Project password evaluation
def check_special_chars(input_string): ## this creates a function to check for special characters
    special_chars = "!@#$%^&*()_+[]{}<>.?/~" ## this is the list of special characters
    for char in input_string:
        if char in special_chars:
            return True
    return False

def check_password(s): ## this creates a function to check the password input
    if len(s) < 8:
        return "password must be at least 8 characters long." ## checks length
    if not any(char.islower() for char in s):
        return "The password must contain lowercase letters." ## checks for lowercase letters
    if not any(char.isupper() for char in s):
        return "The password must contain uppercase letters." ## checks for uppercase letters
    if not any(char.isdigit() for char in s):
        return "The password must contain numbers." ## checks for numbers
    if check_special_chars(s) is False:
        return "The password must contain special characters." ## checks for special characters
    return "The password is good!"


s = input("Please enter a password: ")
print(check_password(s))
