# This assignment focuses on exploring string methods

## Task 1 - string slicing and indexing
s = "Python is amazing!" ## creating the string
print("The string is:", s) ## print the string

slice1 = s[0:7] ## slice one extracts the first 6 characters "Python"
print("First word: " + slice1) ## printing the slice

slice2 = s[10:17] ## slice two extracts the word "amazing"
print("Amazing part of the string: " + slice2) ## printing the slice

slice3 = s[::-1] ## puts the string in reverse order
print("The reversed string: " + slice3) ## printing slice three

## Task 2 - String Methods
s2 = " hello, python world! " ## creating the new string
print(s2) ## printing the string

s2 = s2.strip() ## removing the extra spaces from the string
print(s2) ## printing the previous function

s2 = s2.capitalize() ## capitalizing the first letter
print(s2) ##printing the function

s2 = s2.replace("world", "universe") ## replacing world with universe
print(s2) ## printing the function just performed

s2 = s2.upper() ## making the whole string uppercase
print(s2) ## printing the new string

## Task 3 - Check for palindromes
s3 = str(input("Enter a word to see if it is a palindrome: ")) ## prompting the user to enter a word

s3 = s3.lower().strip() ## makes the string entered lower case

s3r = s3[::-1] ## makes the string reverse

if s3 == s3r:
    print("The word " + s3 + " is a palindrome.")
else:
    print("The word " + s3 + " is not a palindrome.") ## if statement replying to the user whether their word is a palindrome

