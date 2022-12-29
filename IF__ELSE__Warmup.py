length1 = int(input("Enter length of first rectangle: "))
width1 = int(input("Enter width of first rectangle: "))
length2 = int(input("Enter length of second rectangle: "))
width2 = int(input("Enter length of second rectangle: "))

AreaRec1 = length1 * width1
AreaRec2 = length2 * width2

if AreaRec1 > AreaRec2:
    print "Rectangle 1 has a greater area"
    
elif AreaRec1 == AreaRec2:
    print "Rectangles have equal area"

else:
    print "Recrangle 2 has a greater area"
    

