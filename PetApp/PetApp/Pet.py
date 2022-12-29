#define pet class
class pet:

    #the __init__ arguement accepts a name for the pet, their type, and it's type

    def __init__(self,name,type,age):
        self.__name = name
        self.__type = type
        self.__age = age

    #assign a name
    def set_name (self,name):
        self.__name = name
        

    #assign the type of pet
    def set_animal_type (self,type):
        self.__type = type
        

    #assign the age of the pet
    def set_age (self,age):
        self.__age = age
        

    #return name
    def get_name(self):
        return self.__name

    #return type
    def get_type(self):
        return self.__type

    #return age
    def get_age (self):
        return self.__age
