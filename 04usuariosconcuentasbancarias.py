class BankAccount:
	def __init__(self, int_rate = 0.01, balance = 0): 
			self.int_rate = int_rate
			self.balance = balance

	def deposit(self,amount):
		self.balance += amount
		print(f"se realiza un deposito de {amount}, nuevo saldo : {self.balance}")
		return self

	def withdraw(self,amount):
		if self.balance - amount <0:
			print(f"no tiene fondos suficientes, SALDO ACTUAL : {self.balance}")
			return self
		else:
			self.balance -= amount
			print(f"se realiza un retiro de {amount}, SALDO: {self.balance}")
			return self

	def display_account_info(self):
		print(f"el saldo en su cuenta es : {self.balance}")
		return self

	def yield_interest(self):
		self.balance += self.balance*self.int_rate
		print(f"Su cuenta ha aumentado por su tasa de interes de {self.int_rate*100}%, saldo final: {self.balance}")
		return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# agregó esta línea

        
    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
        self.account.deposit(amount)	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        return self
    
    def make_withdrawal(self,amount): #toma un argumento que es el monto del retiro
        self.account.withdraw(amount)#la cuenta del usuario especifico disminuye por la cantidad
        return self

    def display_user_balance(self): #toma el nombre de la instancia y muestra su cuenta bancaria
        self.account.display_account_info()
        return self
    
    # def transfer_money(self, other_user,amount):
    #     if self.account_balance - amount > 0:
    #             self.account_balance -= amount
    #             other_user.account_balance += amount
    #     else:
    #         print(f"{self.name} no tiene fondos suficientes para la transferencia, SALDO ACTUAL : {self.account_balance}")
claudio = User('Claudio','jose.hermosilla@uska.cl')

claudio.make_deposit(100).display_user_balance().make_withdrawal(500)