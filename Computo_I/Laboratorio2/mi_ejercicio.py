# Este código resuelve el problema de un rol de predicación para un mes en una iglesia utilizando 
# principios de Programación Orientada a Objetos (POO). Define dos clases: Predicador, 
# que representa a un predicador con su nombre y el día específico en el que predica, y RolPredicacion, 
# que gestiona la asignación de predicadores a fechas en el calendario. El programa permite al usuario 
# ingresar los nombres de los predicadores para los días de la semana (sábado, miércoles, domingo) y 
# calcula automáticamente qué fechas del mes corresponden a estos días. Finalmente, muestra el rol completo 
# gitcon los días y las fechas asignadas a cada predicador, facilitando así la planificación y coordinación de las predicaciones.

import calendar

# Clase que representa a un predicador
class Predicador:
    def __init__(self, nombre, dia):
        self.nombre = nombre  # Nombre del predicador
        self.dia = dia  # Día de predicación (sábado, miércoles, domingo)

# Clase que gestiona el rol de predicación
class RolPredicacion:
    def __init__(self, mes, anio, predicadores):
        self.mes = mes
        self.anio = anio
        self.predicadores = predicadores
        self.rol = []

    def generar_rol(self):
        calendario = calendar.monthcalendar(self.anio, self.mes)

        for semana in calendario:
            for predicador in self.predicadores:
                dia = semana[predicador.dia]
                if dia != 0:  # Si el día pertenece al mes
                    self.rol.append((calendar.day_name[predicador.dia], dia, predicador.nombre))

    def mostrar_rol(self):
        for dia, fecha, predicador in self.rol:
            print(f"{dia} {fecha}: {predicador}")

# Función para ingresar los nombres de los predicadores
def ingresar_predicadores():
    predicadores = []
    nombres = ["sábado", "miércoles", "domingo"]
    for dia in nombres:
        nombre = input(f"Ingresa el nombre del predicador para el {dia}: ")
        if dia == "sábado":
            predicadores.append(Predicador(nombre, calendar.SATURDAY))
        elif dia == "miércoles":
            predicadores.append(Predicador(nombre, calendar.WEDNESDAY))
        elif dia == "domingo":
            predicadores.append(Predicador(nombre, calendar.SUNDAY))
    return predicadores

# Ejemplo de uso
mes = int(input("Ingresa el mes (número): "))  # Ejemplo: 9 para septiembre
anio = int(input("Ingresa el año: "))  # Ejemplo: 2024

predicadores = ingresar_predicadores()
rol_predicacion = RolPredicacion(mes, anio, predicadores)
rol_predicacion.generar_rol()
rol_predicacion.mostrar_rol()
