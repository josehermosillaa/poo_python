class Tienda:
    def __init__(self,nombre):
        self.nombre = nombre
        self.productos = []
    
    #metodos
    def agregar_producto(self,nuevo_producto):
        print(f"se agrega el producto : {nuevo_producto}")
        self.productos.append(nuevo_producto)
        return self


class Productos:
    def __init__(self, nombre_producto, precio, categoria):
        self.nombre = nombre_producto
        self.precio = precio
        self.categoria = categoria
    #Metodos
    def actualizar_precio(self, porcentaje_cambio, incrementa):
        if incrementa == True:
            print(f'el precio de {self.nombre} aumenta en {porcentaje_cambio}%')
            self.precio += (self.precio)*porcentaje_cambio/100
            print(f"precio final de {self.nombre} : {self.precio}")
            return self
        else:
            print(f'el precio de {self.nombre} disminuye en {porcentaje_cambio}%')
            self.precio -= (self.precio)*porcentaje_cambio/100
            print(f"precio final de {self.nombre} : {self.precio}")
            return self
    
    def imprimir_info(self):
        print(f'''  PRODUCTO
                    nombre: {self.nombre}
                    categoria:{self.categoria}
                    precio: {self.precio}''')
        return self


