# Un concesionario de autos vende vehículos nacionales e importados. Todos tienen 4 ruedas y capacidad para 5 pasajeros. 
# Esta información debe registrarse siempre por razones de ley. Requiere un programa que le permita almacenar las 10 principales 
# características de los autos. El precio de venta de cada auto es igual al precio de compra multiplicado por 1.4 que corresponde
# a su margen de ganancia.

# Clase que representa un vehículo en el concesionario
class Vehiculo:
    def __init__(self, marca, modelo, anio, color, tipo_motor, kilometraje, puertas, equipamiento, pais_origen, precio_compra):
        # Inicializa las 10 características principales del vehículo
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.tipo_motor = tipo_motor  # Tipo de motor (eléctrico, gasolina, diésel, híbrido)
        self.kilometraje = kilometraje  # Kilometraje del vehículo
        self.puertas = puertas  # Número de puertas (2, 4, etc.)
        self.equipamiento = equipamiento  # Equipamiento (básico, intermedio, lujo)
        self.pais_origen = pais_origen  # País de origen del vehículo
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
        self.ruedas = 4  # Todos los vehículos tienen 4 ruedas
        self.capacidad_pasajeros = 5  # Todos los vehículos tienen capacidad para 5 pasajeros

    def calcular_precio_venta(self):
        # Calcula el precio de venta con el margen de ganancia del 40%
        return round(self.precio_compra * 1.4, 2)  # Redondea el precio de venta a 2 decimales

    def mostrar_informacion(self):
        # Muestra en pantalla la información del vehículo
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Color: {self.color}")
        print(f"Tipo de Motor: {self.tipo_motor}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"Puertas: {self.puertas}")
        print(f"Equipamiento: {self.equipamiento}")
        print(f"País de Origen: {self.pais_origen}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de Pasajeros: {self.capacidad_pasajeros}")
        print()

# Ejemplo de uso del programa
vehiculo1 = Vehiculo("Honda", "Civic", 2021, "Negro", "Gasolina", 15000, 4, "Intermedio", "Japón", 18000)
vehiculo2 = Vehiculo("Tesla", "Model S", 2023, "Azul", "Eléctrico", 0, 4, "Lujo", "EE.UU.", 75000)

# Se muestra la información de los vehículos registrados
vehiculo1.mostrar_informacion()
vehiculo2.mostrar_informacion()