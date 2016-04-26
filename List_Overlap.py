#Take two lists, say for example these two:

 # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 #b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
#Make sure your program works on two lists of different sizes.

#Extras:
#Randomly generate two lists to test this
import random
a = random.sample(range(0,100),25)
b = random.sample(range(0,100),30)
c = []
for i in a:
    for item in b:
        if item == i:
             if i in c: #óäàëåíèå ïîâòîðÿþùåãîñÿ ýëåìåíòà, åñëè òàêîâîé çàïèñûâàåòñÿ â ëèñò
                c.pop()
             c.append(i)      
c.sort()     # ñîðòèðîâêà     
print (c)

#another variant
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c =[]
# for el in a:
# if el in b and el not in c:
# c.append(el)
# print c
