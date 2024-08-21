# Clase base
class Mamifero:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Clase derivada
class Domestico(Mamifero):
    def __init__(self, nombre, edad, tipo):
        super().__init__(nombre, edad)
        self.tipo = tipo

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Tipo: {self.tipo}"

# Clase derivada
class Perro(Domestico):
    def __init__(self, nombre, edad, raza, color):
        super().__init__(nombre, edad, "Perro")
        self.raza = raza
        self.color = color

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Raza: {self.raza}, Color: {self.color}"

# Crear objeto
perro1 = Perro("Mingo", 5, "Pitbull", "Rojo Furioso")

# Mostrar datos
print(perro1.mostrar_datos())