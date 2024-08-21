# Una veterinaria atiende solamente perros y los registra en una base de datos. 
# Se requiere un programa que lea la información básica del perro (no más de 8 características) 
# y se muestre en pantalla. En esta veterinaria todos los animales que llegan, entran con el 
# estado inicial de NO ATENDIDO y cuando se registran se cambia automáticamente a ATENDIDO. 
# Por ahora como la veterinaria solo atiende perros, basado en el peso (menos de 10kg o más de 10kg) 
# los registra como “Perro Grande” o “Perro Pequeño”.

# Clase que representa a un perro en la veterinaria
class Perro:
    def __init__(self, nombre, raza, edad, peso, color, nombre_dueño, direccion_dueño, telefono_dueño):
        # Inicializa las características básicas del perro
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.nombre_dueño = nombre_dueño
        self.direccion_dueño = direccion_dueño
        self.telefono_dueño = telefono_dueño
        self.estado = "NO ATENDIDO"  # Estado inicial de todos los perros
        # Determina el tamaño del perro basado en su peso
        self.tamano = "Perro Grande" if peso >= 10 else "Perro Pequeño"
    
    def registrar(self):
        # Cambia el estado a "ATENDIDO" al registrar al perro
        self.estado = "ATENDIDO"
        # Muestra la información del perro en pantalla
        self.mostrar_informacion()
    
    def mostrar_informacion(self):
        # Imprime en pantalla toda la información del perro
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Nombre del Dueño: {self.nombre_dueño}")
        print(f"Dirección del Dueño: {self.direccion_dueño}")
        print(f"Teléfono del Dueño: {self.telefono_dueño}")
        print(f"Estado: {self.estado}")
        print(f"Tamaño: {self.tamano}")

# Solicita la información del perro al usuario
nombre = input("Nombre del perro: ")
raza = input("Raza: ")
edad = int(input("Edad: "))
peso = float(input("Peso (en kg): "))
color = input("Color: ")
nombre_dueño = input("Nombre del dueño: ")
direccion_dueño = input("Dirección del dueño: ")
telefono_dueño = input("Teléfono del dueño: ")

# Crea una instancia de la clase Perro con la información proporcionada
perro = Perro(nombre, raza, edad, peso, color, nombre_dueño, direccion_dueño, telefono_dueño)

# Registra al perro y muestra su información en pantalla
perro.registrar()
