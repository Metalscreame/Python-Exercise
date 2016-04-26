#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num=int(input("Choose a number: "))
limit=int(input("How many numbers do you want to discover?: "))
limit=num*limit+1

firstlist=range(num,limit)
secondlist=[]
for item in firstlist:
    if item % num==0:
        secondlist.append(item)
print(secondlist)