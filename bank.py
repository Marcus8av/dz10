# Превратите функции в методы класса, а параметры в свойства.(банк)

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.operations_count = 0

    def calculate_withdrawal_fee(self, amount):
        fee = amount * 0.015
        return max(fee, 30) if fee <= 600 else 600

    def calculate_tax(self, amount):
        tax = amount * 0.1
        return min(tax, amount)

    def deposit(self, deposit_amount):
        if deposit_amount % 50 != 0:
            print("Сумма пополнения должна быть кратной 50.")
        else:
            self.balance += deposit_amount
            self.operations_count += 1

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount % 50 != 0:
            print("Сумма снятия должна быть кратной 50.")
        elif withdrawal_amount > self.balance:
            print("Недостаточно средств на счете.")
        else:
            fee = self.calculate_withdrawal_fee(withdrawal_amount)
            self.balance -= (withdrawal_amount + fee)
            self.operations_count += 1

    def exit(self):
        return self.balance

    def perform_operations(self):
        while True:
            print("Текущий баланс:", self.balance)
            action = input("Выберите действие (пополнить/снять/выйти): ")

            if action == "пополнить":
                deposit_amount = int(input("Введите сумму для пополнения: "))
                self.deposit(deposit_amount)

            elif action == "снять":
                withdrawal_amount = int(input("Введите сумму для снятия: "))
                self.withdraw(withdrawal_amount)

            elif action == "выйти":
                break

            else:
                print("Неверное действие. Попробуйте ещё раз.")
                continue

            if self.operations_count % 3 == 0:
                interest = self.balance * 0.03
                self.balance += interest

            if self.balance > 5000000:
                tax = self.calculate_tax(self.balance)
                self.balance -= tax

        print("Окончательный баланс:", self.balance)

bank_account = BankAccount()
bank_account.perform_operations()