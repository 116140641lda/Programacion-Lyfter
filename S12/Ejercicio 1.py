class BankAccount:
    def __init__(self, balance):
        try:
            self.balance = float(balance)
        except ValueError:
            print("El balance debe ser numérico")
            self.balance = 0

    def add_money(self, amount):
        try:
            amount = float(amount)
            if amount >= 0:
                self.balance += amount
                print(f"Nuevo Balance: {self.balance}")
            else:
                print("Debe ingresar un monto de depósito correcto")
        except ValueError:
            print("Ingrese valores numéricos únicamente")

    def withdraw_money(self, amount):
        try:
            amount = float(amount)
            if amount > self.balance:
                print("Fondos insuficientes")
            else:
                self.balance -= amount
                print(f"El nuevo balance es de: {self.balance}")
        except ValueError:
            print("Ingrese valores numéricos únicamente")

class SavingAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance) 
        self.min_balance = float(min_balance)

    def withdraw_money(self, amount):
        try:
            amount = float(amount)
            if self.balance - amount < self.min_balance:
                print(f"El balance no puede ser menor al balance mínimo ({self.min_balance})")
            else:
                self.balance -= amount
                print(f"El nuevo balance es de: {self.balance}")
        except ValueError:
            print("Ingrese valores numéricos únicamente")

Person_1 = SavingAccount(200,350)
Person_1.add_money(400)
Person_1.withdraw_money(200)