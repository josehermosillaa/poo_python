from .mathdojo import MathDojo
import unittest
md = MathDojo()
md1 = MathDojo()
class addTests(unittest.TestCase):
    #recordar que cada metodo sera una prueba
    def testList(self):
        self.assertEqual(md.add(1,3,5).result, 9)
    
    def setUp(self):
        # agrega las tareas setUp
        print("running setUp")
    # cualquier tarea que quieras ejecutar después de ejecutar las pruebas, ponlas en el método

    def tearDown(self):
        # agrega las tareas tearDown
        print("running tearDown tasks")

class subtractTests(unittest.TestCase):
    #recordar que cada metodo sera una prueba
    def testList(self):
        self.assertEqual(md1.subtract(-1,-3,5).result, -1)
    
    def setUp(self):
        # agrega las tareas setUp
        print("running setUp")
    # cualquier tarea que quieras ejecutar después de ejecutar las pruebas, ponlas en el método

    def tearDown(self):
        # agrega las tareas tearDown
        print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main()  # esto ejecuta nuestras pruebas
#prueba
# md = MathDojo()
# # para probar:copy
# x = md.add(2).add(2, 5, 1).subtract(3, 2)
# md.desviacion_estandar()

