class BankAccount :
    balance = 0
    def __init__(self, balance):
        self.balance = balance

    def add_money (self,amount):
        self.balance += amount
        print(f"Nuevo Balance : {self.balance}")

    def withdraw_money (self,amount):
        
        if amount > self.balance:
            print("Fondos insuficientes")
        else:
            self.balance -= amount
            print(f"El nuevo balance es de : {self.balance}")

class SavingAccount(BankAccount):

    def __init__(self,min_balance):
    
        self.min_balance = min_balance


    def withdraw_money (self,amount):

        if self.balance - amount < self.min_balance :
            print(f"El balance no puede ser menor al balance minimo,{self.min_balance} ")

        else:
            self.balance -= amount
            print(f"El nuevo balance es de : {self.balance}")

Person_1 = SavingAccount(350)
Person_1.add_money(800)
Person_1.withdraw_money(200)