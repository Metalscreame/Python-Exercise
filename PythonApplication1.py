#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number=int(input("Print the number: "))
if number % 2 == 0:
    print("Its Odd!!!!!!!!YESSS")
else: 
    print("Its even :( ")

#extra
print("Yol'll be asked for two numbers: one number to check and number to devide by")
num=int(input("Print number to check: "))
check=int(input("Print number to devide: "))

if num % check == 0:
    print("The num is devided by",check)
else:
    print("Thu num ISNT devided by",check)