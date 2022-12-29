import bankaccount

def main():
    #get the starting blance from the user
    startBal = float(input('Enter your starting balance: '))

    #create the new bankaccount object
    savings = bankaccount.BankAccount(startBal)

    #deposit a pay check
    pay = float(input('How much was your paycheck?'))
    print('Depositing check')
    savings.deposit(pay)

    #display the balance
    print('Your account balance is: $', format(savings.getBalance(), ',.2f'), sep='')

    #get the withdraw amount
    cash = float(input('How much would you like to withdraw?'))
    print('I will withdraw that from your acounnt')
    savings.withdraw(cash)
    
    #display the balance
    print('Your account balance is: $', format(savings.getBalance(), ',.2f'), sep='')

main()
