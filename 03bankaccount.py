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
			print(f"no tiene fondos suficientes")
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

cuenta1 = BankAccount()
cuenta2 = BankAccount(0.02,100)
cuenta1.deposit(100).deposit(500).deposit(700).withdraw(1100).yield_interest().display_account_info()

cuenta2.deposit(300).deposit(500).withdraw(700).withdraw(20).withdraw(50).withdraw(1).yield_interest().display_account_info()
