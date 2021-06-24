# reverseList : escribe una función que invierta los valores en la lista (sin crear una matriz temporal).
# Ejemplo: reverseList ([1,3,5]) debería devolver [5,3,1]
# Prueba de ejemplo: afirmarEqual (reverseList ([1,3,5]), [5,3,1])
import unittest

def listainversa(list):
    for i in range(0,int(len(list)/2)):
        a = list[len(list)-1-i]
        b = list[i]
        list[i] = a
        list[len(list)-1-i] = b
        print(list)
    # print(list)
    return list
#vamos con los tests
class listainversaTests(unittest.TestCase):
    #recordar que cada metodo sera una prueba
    def testList(self):
        self.assertEqual(listainversa([1,3,5]),[5,3,1])
    
    def setUp(self):
        # agrega las tareas setUp
        print("running setUp")
    # cualquier tarea que quieras ejecutar después de ejecutar las pruebas, ponlas en el método

    def tearDown(self):
        # agrega las tareas tearDown
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main()  # esto ejecuta nuestras pruebas
# Agregue al menos otros 3 casos de prueba
# isPalindrome : escribe una función que verifique si la palabra dada es palíndrome (una palabra que se lee igual en ambos sentidos).
# Ejemplo: isPalindrome ("racecar") debería devolver True
# Prueba de ejemplo: afirmarEqual (isPalindrome ("racecar"), True) o afirmarTrue (isPalindrome ("racecar"))
# Prueba de ejemplo: afirmarFalse (isPalindrome ("rabcr")).
# Agregue al menos otros 5 casos de prueba
# monedas : escribe una función que determine cuántas monedas de 25 centavos, de 10 centavos, de 5 centavos y de 1 centavo le dará a un cliente para un cambio en el que minimice la cantidad de monedas que entrega.
# Ejemplo: dado 87 centavos, el resultado debe ser 3 cuartos, 1 centavo, 0 níquel y 2 centavos
# Prueba de ejemplo: afirmar Igual (moneda (87), [3,1,0,2])
# Agregue al menos otros 5 casos de prueba
# BONUS - factorial - Escribe una función recursiva que devuelve el factorial de un número dado. Recuerde que el factorial de un número es el producto de todos los números entre 1 y el número dado (por ejemplo, 4! = 4 * 3 * 2 * 1).
# Ejemplo: factorial (5) debería devolver 120.
# Agregue al menos 3 casos de prueba
# BONUS - fibonacci - Escribe una función recursiva que acepta un número, n, y devuelve el enésimo número de Fibonacci de la secuencia. Los primeros dos números de Fibonacci son 0 y 1. Cada número posterior se calcula sumando los 2 números anteriores de la secuencia. (es decir, 0, 1, 1, 2, 3, 5, 8, 13, 21 ...)
# Ejemplo: fibonacci (5) debería devolver 3 (el quinto número en la secuencia es 3).
# Agregue al menos 3 casos de prueba'''