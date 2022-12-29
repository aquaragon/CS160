#Get building cost from user
cost = int(input("Enter the cost of the building: "))

#calculate fee
if cost <= 5000:
    fee = .08 * cost
else:
    remainder = cost - 5000
    fee = .08 * 5000
    if remainder <= 80000:
        fee = fee + ( .03 * remainder )
    else:
        fee = fee + ( .025 * remainder ) 

#displaying result
print("The architect's fee is:$" + format(fee,'.2f')) 
