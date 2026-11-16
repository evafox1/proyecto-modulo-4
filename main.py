
# Clase Alumno
class Alumno:
    def __init__(self, nombre, matricula, calificaciones):
        self.nombre = nombre
        self.matricula = matricula
        self.calificaciones = calificaciones

    def calcular_promedio(self):
        suma = 0
        for calificacion in self.calificaciones:
            suma += calificacion

        promedio = suma / len(self.calificaciones)
        return promedio


# Lista para almacenar los alumnos
alumnos = []

# Solicitar cantidad de alumnos
cantidad = int(input("¿Cuantos alumnos desea registrar? "))

# Registrar alumnos
for i in range(cantidad):
    print(f"Registro del alumno {i + 1}")

    nombre = input("Nombre: ")
    matricula = input("Matricula: ")

    calificaciones = []

    for j in range(3):
        calificacion = int(input(f"Calificacion {j + 1}: "))
        calificaciones.append(calificacion)

    alumno = Alumno(nombre, matricula, calificaciones)
    alumnos.append(alumno)


# Resultados

suma_promedios = 0
promedio_mayor = 0
promedio_menor = 100

for alumno in alumnos:
    promedio = alumno.calcular_promedio()

    print(f"Alumno: {alumno.nombre}")
    print(f"Matricula: {alumno.matricula}")
    print(f"Calificaciones: {alumno.calificaciones}")
    print(f"Promedio: {promedio:.2f}")

    suma_promedios += promedio

    if promedio > promedio_mayor:
        promedio_mayor = promedio

    if promedio < promedio_menor:
        promedio_menor = promedio


# Estadisticas del grupo
promedio_general = suma_promedios / cantidad

print("Estadisticas del grupo")
print(f"Promedio mayor: {promedio_mayor:.2f}")
print(f"Promedio menor: {promedio_menor:.2f}")
print(f"Promedio general: {promedio_general:.2f}")
