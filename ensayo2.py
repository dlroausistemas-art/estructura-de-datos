notas = []
for estudiante in range(3):
    print("\nEstudiante", estudiante + 1)

    nombre = input("Ingrese el nombre: ")

    programacion = float(input("Nota de Programación: "))
    matematicas = float(input("Nota de Matemáticas: "))
    ingles = float(input("Nota de Inglés: "))

    notas.append([nombre, programacion, matematicas, ingles])


print("\nPROMEDIO DE CADA ESTUDIANTE")

for estudiante in notas:
    nombre = estudiante[0]

    suma = estudiante[1] + estudiante[2] + estudiante[3]

    promedio = suma / 3

    print(nombre, "- Promedio:", promedio)
    print(notas)