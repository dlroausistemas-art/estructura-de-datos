while True:
    nombre = input("Ingrese su nombre: ")
    notas = []
    estudiantes = []
    for i in range(3):
        notas.append(float(input("Ingrese la nota " + str(i+1) + ": ")))
    estudiantes.append([nombre] + notas)
    
    