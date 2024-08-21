# Una papelería vende cuadernos y lápices. Los cuadernos pueden ser de 50 hojas o de 100 hojas. 
# Los lápices pueden ser de grafito o de colores. El precio de venta es igual al precio de compra 
# multiplicado por 1.30 que corresponde al margen de ganancia. La papelería requiere construir un 
# programa que le permita registrar y visualizar por lo menos dos artículos de ítem. Todos los 
# cuadernos son marca HOJITAS y los lápices son marca RAYAS ya que la papelería es un distribuidor exclusivo.

# Clase base que representa un artículo en la papelería
class Articulo:
    def __init__(self, nombre, tipo, precio_compra):
        # Inicializa las características básicas del artículo
        self.nombre = nombre
        self.tipo = tipo
        self.precio_compra = precio_compra
        # Calcula el precio de venta con el margen de ganancia del 30%
        self.precio_venta = self.calcular_precio_venta()
    
    def calcular_precio_venta(self):
        # Calcula el precio de venta basado en el precio de compra
        return self.precio_compra * 1.30
    
    def mostrar_informacion(self):
        # Muestra la información del artículo en pantalla
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")
        print()

# Clase que representa un cuaderno, hereda de Articulo
class Cuaderno(Articulo):
    def __init__(self, hojas, precio_compra):
        nombre = "Cuaderno"
        tipo = f"Cuaderno de {hojas} hojas"
        # Llama al constructor de la clase base
        super().__init__(nombre, tipo, precio_compra)
        # Todos los cuadernos son de la marca HOJITAS
        self.marca = "HOJITAS"

    def mostrar_informacion(self):
        # Muestra la marca del cuaderno y la información básica del artículo
        print(f"Marca: {self.marca}")
        super().mostrar_informacion()

# Clase que representa un lápiz, hereda de Articulo
class Lapiz(Articulo):
    def __init__(self, tipo_lapiz, precio_compra):
        nombre = "Lápiz"
        tipo = f"Lápiz de {tipo_lapiz}"
        # Llama al constructor de la clase base
        super().__init__(nombre, tipo, precio_compra)
        # Todos los lápices son de la marca RAYAS
        self.marca = "RAYAS"

    def mostrar_informacion(self):
        # Muestra la marca del lápiz y la información básica del artículo
        print(f"Marca: {self.marca}")
        super().mostrar_informacion()

# Uso del programa: se crean instancias de cuadernos y lápices
cuaderno1 = Cuaderno(50, 10.0)
cuaderno2 = Cuaderno(100, 15.0)

lapiz1 = Lapiz("grafito", 5.0)
lapiz2 = Lapiz("colores", 7.0)

# Se muestra la información de los artículos registrados
cuaderno1.mostrar_informacion()
cuaderno2.mostrar_informacion()
lapiz1.mostrar_informacion()
lapiz2.mostrar_informacion()
