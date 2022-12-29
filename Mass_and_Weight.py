mass = float(input("Mass in kilograms? "))
constant = float(9.8)
weight = (mass * constant)
if weight > int(500):
    print(format(weight, '.2f') + "N is too heavy")
elif weight < int(100):
    print(format(weight, '.2f') + "N is too light")
else:
    print("Your weight is " + format(weight, '.2f') + "N")  
                   
