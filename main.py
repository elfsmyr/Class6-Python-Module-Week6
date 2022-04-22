import bank
import client
bank_account=bank.Bank("ING")
amounts={}
       
def add(): 
        print("To create an account, please fill in the information below.")
        name=input("Name:")
        deposit_amount=input("Deposit amount:")
        amounts[name]=deposit_amount
        new_account=client.Client(name,deposit_amount)
        bank_account.add_client(new_account.account_number,new_account.name)
        print('''Account created successfully! Your account number is:{}'''.format(new_account.account_number))
        
def control():
        print("To access your account, please enter your credentials below.")
        name=input("Name:")
        account_number=input("Account Number:")
        new_account=client.Client(name,amounts[name])
        result=bank_account.authentication(name,account_number)
        if result==False:
            print('''Authentication failed!
Reason: account not found.''')
        elif result==True:
            print('''Authentication successful!

Welcome {}!'''.format(name))
            while True:
               print('''Choose an option:

    1. Withdraw
    2. Deposit
    3. Balance
    4. Exit''')
               choose1=int(input("your choose:"))
               if choose1==1:
                    amount=int(input("witdraw amount:"))
                    new_balance=new_account.withdraw(amount)
                    if new_balance<0:
                        print("Insufficient Balance")
                    else:
                        print('''The sum of {} has been withdrawn from your account balance.

Your current account balance is: {}'''.format(amount,new_balance))
               elif choose1==2:
                   amount=int(input("Deposit amount:"))
                   new_balance=new_account.deposit(amount)
                   print('''The sum of {} has been added to your account balance.

Your current account balance is: {}'''.format(amount,new_balance))
               elif choose1==3:
                   print("Your current account balance is: {}".format(new_account.balance()))
               elif choose1==4:
                   break
        
while (True):
    print('''
Welcome to {}!

Choose an option:

    1. Open new bank account
    2. Open existing bank account
    3. Exit'''.format(bank_account.name))
    choose=int(input("your choose:"))
    if choose==1:
       add()
    elif choose==2:
       control()
               
    elif choose==3:
        break
                    
