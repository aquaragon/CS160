W_o_P = float(input("Please enter weight of package in pounds: "))

if W_o_P <= 2:
    cost = W_o_P * 1.50
    print("Your shipping charges are: $" + format(cost, '.2f'))
elif W_o_P > 2 and W_o_P <= 6:
    cost = W_o_P * 3.00
    print("Your shipping charges are: $" + format(cost, '.2f'))
elif W_o_P > 6 and W_o_P <= 10:
    cost = W_o_P * 4.00
    print("Your shipping charges are: $" + format(cost, '.2f'))
else:
    cost = W_o_P * 4.75
    print("Your shipping charges are: $" + format(cost, '.2f'))
                
