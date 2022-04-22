import random
class Client:
    def __init__(self,name,total_amount) :
        self.account_number=random.randint(10000,99999)
        self.name=name
        self.total_amount=total_amount
    def withdraw(self,amount):
        self.amount=amount
        if int(self.total_amount)>amount:
            self.total_amount=int(self.total_amount)-amount
            return self.total_amount
        else:
            return -1
    def deposit(self,amount):
        self.amount=amount
        self.total_amount=int(self.total_amount)+amount
        return self.total_amount
    def balance(self):
        return self.total_amount
    