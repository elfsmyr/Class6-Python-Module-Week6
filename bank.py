import client
class Bank:
    client={}
    def __init__(self,name):
        self.name=name
    
    def add_client(self,account_number,name):
        self.account_number=account_number
        self.name=name
        self.client[self.name]=self.account_number
        
    def authentication(self,name,account_number):
        self.name=name
        self.account_number=account_number
        
        for i in self.client:            
          if i==name:
              if int(account_number)==int(self.client[name]):
                   result=True
                   break
              else: 
                   result=False
          else:
              result=False
        return result
        