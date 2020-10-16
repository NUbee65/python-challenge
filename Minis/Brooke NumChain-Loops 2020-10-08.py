# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 14:59:28 2020

@author: brook
"""
# initialize variables
counter = 0
x = 0
y = 0
z = "yes"

# x is the initial number of numbers chosen by user to be listed
x = int(input("How many numbers would you like to list?  "))
print()
    
for x in range(0, (x + 1)) :
    print(x)
    counter = (x + 1)

z = input("Would you like to continue? yes/no  ")

while z == "yes" :
    
    # y is the subsequent number of numbers chosen by user to be listed
    y = int(input("How many numbers would you like to list this time, continuing from where we left off?  "))
    print()
    
    for y in range(counter, counter + y) :
        print(y)
        counter = y + 1

    z = input("Would you like to continue? yes/no  ")

else :
   print("Thank you for playing!  Hope you'll play again.")
    