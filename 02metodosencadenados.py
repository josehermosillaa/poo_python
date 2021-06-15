class User:
    def __init__(self, username, email_address):# ahora nuestro método tiene 2 parametros!
        self.name = username			#y usamos los valores pasados para establecer el atributo de nombre
        self.email = email_address		# y el atributo email
        self.account_balance = 0		# el saldo de la cuenta se establece en $ 0, así que no es necesario un tercer parámetro
    
# agrega el método deposit 
    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
        self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        return self
    
    def make_withdrawal(self,amount): #toma un argumento que es el monto del retiro
        self.account_balance -= amount #la cuenta del usuario especifico disminuye por la cantidad
        return self
    
    def display_user_balance(self): #toma el nombre de la instancia y muestra su cuenta bancaria
        print(self.account_balance)
        return self
    
    def transfer_money(self, other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
jose = User("Jose Hermosilla","jose.hermosilla@usach.cl")
print(guido.name)	# salida: Guido van Rossum
print(monty.name)	# salida: Monty Python
print(jose.name)

guido.make_deposit(100).make_deposit(200).make_deposit(150).make_withdrawal(350)
print(guido.account_balance)

monty.make_deposit(50).make_deposit(500).make_withdrawal(150).make_withdrawal(320)
print(monty.account_balance)


jose.make_deposit(1000).make_withdrawal(350).make_withdrawal(59).make_withdrawal(1)
print(jose.account_balance)


guido.transfer_money(monty,1000)
monty.transfer_money(jose,250)
print(f"guido tiene {guido.account_balance} en su cuenta")
guido.make_deposit(1000)
print(guido.account_balance)
monty.make_withdrawal(50)
print(f"monty: {monty.account_balance}") #deberia ser 1000 por el transfer
print(f"jose :{jose.account_balance}")