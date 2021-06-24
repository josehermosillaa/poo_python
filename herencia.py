# class CheckingAccount:
#     def __init__(self, int_rate, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance

#     def deposit(self, amount):
#         # code

#     def withdraw(self, amount):
#         # code

#     def write_check(self, amount):
#         # code

#     def display_account_info(self):
#         # code

# class RetirementAccount:

#     def __init__(self, int_rate, is_roth, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#         self.is_roth = is_roth

#     def deposit(self, amount):w
#         # código - evaluar impuestos si es necesario

#     def withdraw(self, amount):
#         # código - evaluar impuestos si es necesario

#     def display_account_info(self):
#         # codigo

'''esto se siente repetitivo, por lo que la herencia permite un equilibrio: nos permite tener una clase principal que contiene los
atributos y metodos que sean comunes entre las nuevas clases. a su vez, cada clase secundaria solo contendra
lo que es exclusivo de esa clase '''

# class CheckingAccount(BankAccount):
#     pass

# class RetirementAccount(BankAccount):
#     pass
# Super : Esto es lo que queremos que haga nuestro método RetirementAccount__init__. y lo que hace nuestro metodo
# principal de la clase BankAccount

'''
class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.is_roth = is_roth'''


class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("INSUFFICIENT FUNDS")
        return self
# la clase BankAccount ya hace 2 de las 3 lineas que estamos tratando de ejecutar de nuestra clase


class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth

    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        super().withdraw(amount)
        return self


'''podemos heredar funciones para no repetir'''

# class RetirementAccount(BankAccount):
#     def withdraw(self, amount, is_early):
#         if is_early:
#             amount = amount * 1.10
#         if (self.balance - amount) > 0:
#             self.balance -= amount
#         else:
#             print("INSUFFICIENT FUNDS")
#         return self


# class BankAccount:
#     def withdraw(self, amount):
#         if (self.balance - amount) > 0:
#             self.balance -= amount
#         else:
#             print("INSUFFICIENT FUNDS")
#         return self


'''esto sin herencia, en cambio podemo0s ver que se heredan las funcion es repetitivas igual'''

pedro = RetirementAccount(1,True)
pedro.withdraw(100,True)
