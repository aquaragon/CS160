base_price = float(72.00)


#get single-day tickets from user
SDT = int(input("Enter the number of tickets "))

#get membership type
Membership = (input("Enter membership type "))

#total cost without discount
Without_discount = float(base_price * SDT)

#determine membership discount
if Membership == "AAA":
    print("Your purchase price is: $" + format((Without_discount * .85), '.2f'))
elif Membership == "AARP":
    print("Your purchase price is: $" + format((Without_discount * .825), '.2f'))
elif Membership == "Military ID":
    print("Your purchase price is: $" + format((Without_discount * .8), '.2f'))
else:
    print ("Your purchase price is: $" + format(Without_discount, '.2f'))

