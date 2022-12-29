#class to simulate the way a bank account works
class BankAccount:
    #the __init__ method accepts an arguement for the account's balance
    #It is assigned to the __balance attribute

    def __init__(self, bal):
        self.__balance = bal

    #deposit method adds to the balance of the account
    def deposit(self, amount):
            self.__balance += amount
    
    #withdraw method subtracts from the balance of the amount
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print ('Error: Insufficient funds')

    #getBalance will return the current balance in the account
    def getBalance(self):
        return self.__balance
