# Un almacén vende dispositivos electrónicos (celulares, tablets y portá- tiles). Todos PHR que es una nueva marca 
# que está entrando en el mercado. Se requiere almacenar sus 6 principales características. Todos son productos 
# importados y su precio de venta es igual al precio de compra multiplicado por 1.7 que corresponde a su margen de ganancia.

# Clase que representa un dispositivo electrónico en el almacén
class DispositivoElectronico:
    def __init__(self, tipo, modelo, tamano_pantalla, almacenamiento, procesador, memoria, precio_compra):
        # Inicializa las características principales del dispositivo
        self.tipo = tipo
        self.marca = "PHR"  # Todos los dispositivos son de la marca PHR
        self.modelo = modelo
        self.tamano_pantalla = tamano_pantalla  # Tamaño de la pantalla en pulgadas
        self.almacenamiento = almacenamiento  # Almacenamiento en GB
        self.procesador = procesador  # Tipo de procesador
        self.memoria = memoria  # Memoria RAM en GB
        self.precio_compra = precio_compra  # Precio de compra del dispositivo
        self.precio_venta = self.calcular_precio_venta()
        self.origen = "Importado"  # Todos los dispositivos son importados

    def calcular_precio_venta(self):
        # Calcula el precio de venta basado en el margen de ganancia del 70%
        return round(self.precio_compra * 1.7, 2)

    def mostrar_informacion(self):
        # Muestra en pantalla la información del dispositivo
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca} | Modelo: {self.modelo}")
        print(f"Tamaño de Pantalla: {self.tamano_pantalla} pulgadas")
        print(f"Almacenamiento: {self.almacenamiento} GB | Procesador: {self.procesador}")
        print(f"Memoria RAM: {self.memoria} GB")
        print(f"Precio de Compra: ${self.precio_compra:.2f} | Precio de Venta: ${self.precio_venta:.2f}")
        print(f"Origen: {self.origen}")
        print()

# Lista de dispositivos electrónicos a registrar
dispositivos = [
    DispositivoElectronico("Celular", "Z9 Pro", 6.8, 256, "Snapdragon 895", 12, 400.0),
    DispositivoElectronico("Tablet", "Tab Max", 12.4, 512, "Apple M1", 8, 800.0),
    DispositivoElectronico("Portátil", "Notebook X", 14.0, 1024, "Intel Core i9", 32, 1500.0)
]

# Mostrar la información de todos los dispositivos registrados
for dispositivo in dispositivos:
    dispositivo.mostrar_informacion()