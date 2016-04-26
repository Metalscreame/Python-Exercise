#Ask the user for a string and print out whether this string is a palindrome or not. 
#(A palindrome is a string that reads the same forwards and backwards.)

user_string=str(input("Print a string: "))
reversed_string=user_string[::-1]
if user_string==reversed_string:
     print ("The string is a palindrome")
else:
    print("String is not a palindrome")
