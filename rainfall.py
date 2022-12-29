years = int(input("How many years? "))
yearsave = years
rainfall = 0
if (years < 0):
    years = input ("Can't be negative, How many years? ")
while (years > 0):
    years = years - 1
    months = 0
    while (months < 12):
        rainfall = rainfall + int(input("How many inches of rain this month? "))
        if (rainfall - (rainfall * months)) > 60 or rainfall < 0:
            rainfall = rainfall + int(input("Invalid entry, How many inches of rain this month? "))
        months = months + 1
print("Total months: ", (12 * yearsave))
print("Inches of rainfall: ", rainfall)
print("Average rainfall per month: ", rainfall/(12 * yearsave))
        
    
