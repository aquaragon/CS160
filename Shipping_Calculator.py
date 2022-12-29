#get purchase amount
items = int(input("Enter amount items purchased "))

#intial costant cost
INTIAL = 2.99

#calculate costs
if (items == 1):
    print ("Your shipping costs is: $" + str(INTIAL))
elif (items >= 2 and items <= 5):
    print ("Your shipping costs is: $", format(INTIAL + (1.99*(items-1)),'.2f'))
elif (items > 5 and items < 15):
    print ("Your shipping costs is: $", format(INTIAL + (1.99*4) + (1.49*(items-5)),'.2f'))
elif (items >=15):
    print ("Your shipping costs is: $", format(INTIAL + (1.99*4) + (1.49*9) + (.99*(items-14)),'.2f'))
