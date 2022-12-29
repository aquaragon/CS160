import Pet

def main():
    #inputs animal name from user
    name = str(input("What is the pet's name? "))

    #inputs animal type from user
    type = str(input("What type of pet is it? "))

    #inputs animal age from user
    age= int(input("How old is the pet? "))
    NewPet = Pet.pet(name,type,age)
    print ("Your pet's name is: ", NewPet.get_name())

    print ("Your pet's type is: ", NewPet.get_type())

    print ("Your pet's age is: ", NewPet.get_age())
    
main()