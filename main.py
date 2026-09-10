# =============================================================================
# PARTE 1. Recordación básica
# Ejercicio 1 — Información personal
# =============================================================================
def ejercicio_1():
    print("\n--- EJERCICIO 1: INFORMACIÓN PERSONAL ---")
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    programa = input("Ingrese su programa académico: ")
    semestre = int(input("Ingrese su semestre: "))

    print("\n=================================")
    print(" INFORMACIÓN DEL ESTUDIANTE ")
    print("=================================")
    print(f"Nombre:   {nombre}")
    print(f"Edad:     {edad} años")
    print(f"Programa: {programa}")
    print(f"Semestre: {semestre}")

# =============================================================================
# PARTE 2. Condicionales
# Ejercicio 2 — Estado académico
# =============================================================================
def ejercicio_2():
    print("\n--- EJERCICIO 2: ESTADO ACADÉMICO ---")
    try:
        nota = float(input("Ingrese la nota definitiva (0.0 a 5.0): "))
        if nota < 0.0 or nota > 5.0:
            print("Error: La nota no es válida. Debe estar entre 0.0 y 5.0.")
        elif nota >= 3.0:
            print(f"Nota: {nota} -> APROBADO")
        else:
            print(f"Nota: {nota} -> REPROBADO")
    except ValueError:
        print("Error: Debe ingresar un valor numérico.")

# =============================================================================
# PARTE 3. Ciclos
# Ejercicio 3 — Números
# =============================================================================
def ejercicio_3():
    print("\n--- EJERCICIO 3: NÚMEROS (1 AL 100) ---")
    
    # 1. Todos los números del 1 al 100
    print("\n1. Números del 1 al 100:")
    for i in range(1, 101):
        print(i, end=" ")
    print()

    # 2. Números pares
    print("\n2. Números pares del 1 al 100:")
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, end=" ")
    print()

    # 3. Números impares
    print("\n3. Números impares del 1 al 100:")
    for i in range(1, 101):
        if i % 2 != 0:
            print(i, end=" ")
    print()

    # 4. Múltiplos de 5
    print("\n4. Múltiplos de 5 del 1 al 100:")
    for i in range(1, 101):
        if i % 5 == 0:
            print(i, end=" ")
    print()

    # 5. Suma acumulada de todos los números
    suma_total = 0
    for i in range(1, 101):
        suma_total += i
    print(f"\n5. La suma de todos los números del 1 al 100 es: {suma_total}")

# =============================================================================
# PARTE 4. Funciones
# Ejercicio 4 — Calculadora
# =============================================================================
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

def ejercicio_4():
    while True:
        print("\n=========================")
        print(" CALCULADORA ")
        print("=========================")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        if opcion == "5":
            print("Saliendo de la calculadora...")
            break
        elif opcion in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                
                if opcion == "1":
                    print(f"Resultado: {num1} + {num2} = {sumar(num1, num2)}")
                elif opcion == "2":
                    print(f"Resultado: {num1} - {num2} = {restar(num1, num2)}")
                elif opcion == "3":
                    print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
                elif opcion == "4":
                    res = dividir(num1, num2)
                    print(f"Resultado: {res}")
            except ValueError:
                print("Error: Por favor ingrese valores numéricos válidos.")
        else:
            print("Opción inválida. Intente de nuevo.")

# =============================================================================
# PARTE 5. Primer contacto con estructuras de datos
# Ejercicio 5 — Muchas variables... ¿un problema?
# =============================================================================
def ejercicio_5():
    print("\n--- EJERCICIO 5: MUCHAS VARIABLES ---")
    nota1 = 3.5
    nota2 = 4.2
    nota3 = 2.8
    nota4 = 4.5
    nota5 = 3.9

    # Cálculo manual inicial con variables individuales
    suma = nota1 + nota2 + nota3 + nota4 + nota5
    promedio = suma / 5

    # Determinar mayor y menor manualmente
    mayor = nota1
    if nota2 > mayor: mayor = nota2
    if nota3 > mayor: mayor = nota3
    if nota4 > mayor: mayor = nota4
    if nota5 > mayor: mayor = nota5

    menor = nota1
    if nota2 < menor: menor = nota2
    if nota3 < menor: menor = nota3
    if nota4 < menor: menor = nota4
    if nota5 < menor: menor = nota5

    # Contar aprobados
    aprobados = 0
    if nota1 >= 3.0: aprobados += 1
    if nota2 >= 3.0: aprobados += 1
    if nota3 >= 3.0: aprobados += 1
    if nota4 >= 3.0: aprobados += 1
    if nota5 >= 3.0: aprobados += 1

    print(f"Promedio: {promedio:.2f}")
    print(f"Mayor nota: {mayor}")
    print(f"Menor nota: {menor}")
    print(f"Cantidad de aprobados: {aprobados}")

# =============================================================================
# PARTE 6. Mi primera lista
# Ejercicio 6 — Estudiantes
# =============================================================================
def ejercicio_6():
    print("\n--- EJERCICIO 6: LISTA DE ESTUDIANTES ---")
    estudiantes = ["Carlos", "María", "Juan", "Ana", "Pedro", 
                   "Luisa", "Andrés", "Sofia", "Diego", "Laura"]

    print(f"7. Lista completa: {estudiantes}")
    print(f"8. Primer estudiante: {estudiantes[0]}")
    print(f"9. Último estudiante: {estudiantes[-1]}")
    print(f"10. Cantidad de estudiantes: {len(estudiantes)}")

    # 11. Agregar estudiante
    nuevo = "Gabriel"
    estudiantes.append(nuevo)
    print(f"11. Estudiante '{nuevo}' agregado. Nueva lista: {estudiantes}")

    # 12. Eliminar estudiante
    eliminado = "Juan"
    if eliminado in estudiantes:
        estudiantes.remove(eliminado)
        print(f"12. Estudiante '{eliminado}' eliminado. Nueva lista: {estudiantes}")

    # 13. Buscar estudiante
    buscado = "Sofia"
    if buscado in estudiantes:
        pos = estudiantes.index(buscado)
        print(f"13. Estudiante '{buscado}' encontrado en la posición {pos}.")
    else:
        print(f"13. Estudiante '{buscado}' no encontrado.")

# =============================================================================
# PARTE 7. Trabajando con datos
# Ejercicio 7 — Notas (Sin utilizar max(), min() ni sum())
# =============================================================================
def ejercicio_7():
    print("\n--- EJERCICIO 7: PROCESAMIENTO DE NOTAS CON CICLOS ---")
    notas = [3.5, 4.2, 2.8, 4.5, 3.9, 2.5, 4.0, 4.7]

    # 14. Número de estudiantes
    num_estudiantes = len(notas)

    # Acumuladores y banderas para cálculo manual
    suma_notas = 0
    nota_mayor = notas[0]
    nota_menor = notas[0]
    aprobados = 0
    reprobados = 0

    for nota in notas:
        suma_notas += nota
        if nota > nota_mayor:
            nota_mayor = nota
        if nota < nota_menor:
            nota_menor = nota
        if nota >= 3.0:
            aprobados += 1
        else:
            reprobados += 1

    promedio = suma_notas / num_estudiantes

    # 20. Notas mayores que el promedio
    mayores_promedio = []
    for nota in notas:
        if nota > promedio:
            mayores_promedio.append(nota)

    print(f"14. Número de estudiantes: {num_estudiantes}")
    print(f"15. Promedio: {promedio:.2f}")
    print(f"16. Nota mayor: {nota_mayor}")
    print(f"17. Nota menor: {nota_menor}")
    print(f"18. Cantidad de aprobados: {aprobados}")
    print(f"19. Cantidad de reprobados: {reprobados}")
    print(f"20. Notas mayores que el promedio ({promedio:.2f}): {mayores_promedio}")

# =============================================================================
# PARTE 8. Buscar información
# Ejercicio 8 — Búsqueda
# =============================================================================
def ejercicio_8():
    print("\n--- EJERCICIO 8: BÚSQUEDA EN LISTA ---")
    productos = [
        "Teclado",
        "Mouse",
        "Monitor",
        "Impresora",
        "Memoria RAM",
        "Disco SSD"
    ]

    busqueda = input("Ingrese el producto a buscar: ").strip()

    encontrado = False
    posicion = -1

    # Recorrido secuencial (búsqueda lineal)
    for i in range(len(productos)):
        if productos[i].lower() == busqueda.lower():
            encontrado = True
            posicion = i
            break

    if encontrado:
        print(f"¡El producto '{productos[posicion]}' fue ENCONTRADO en la posición {posicion}!")
    else:
        print(f"El producto '{busqueda}' NO fue encontrado en la lista.")

# =============================================================================
# PARTE 9. Matrices
# Ejercicio 9 — Notas de un grupo
# =============================================================================
def ejercicio_9():
    print("\n--- EJERCICIO 9: MATRICES Y CALIFICACIONES ---")
    # Filas: Estudiantes (0 a 4)
    # Columnas: 0 = Programación, 1 = Matemáticas, 2 = Inglés
    notas = [
        [4.0, 3.5, 4.2],
        [3.0, 4.1, 3.7],
        [4.5, 3.8, 4.0],
        [2.8, 3.2, 3.5],
        [3.9, 4.5, 4.2]
    ]

    # 1. Promedio por estudiante
    print("\n1. Promedio por estudiante:")
    for idx, estudiante in enumerate(notas):
        suma_est = 0
        for nota in estudiante:
            suma_est += nota
        prom_est = suma_est / len(estudiante)
        print(f"   Estudiante {idx + 1}: {prom_est:.2f}")

    # 2. Promedio por asignatura
    asignaturas = ["Programación", "Matemáticas", "Inglés"]
    print("\n2. Promedio por asignatura:")
    num_filas = len(notas)
    num_columnas = len(notas[0])

    for col in range(num_columnas):
        suma_asig = 0
        for fila in range(num_filas):
            suma_asig += notas[fila][col]
        prom_asig = suma_asig / num_filas
        print(f"   {asignaturas[col]}: {prom_asig:.2f}")

    # 3 y 4. Nota mayor y nota menor de toda la matriz
    nota_mayor = notas[0][0]
    nota_menor = notas[0][0]

    for fila in notas:
        for nota in fila:
            if nota > nota_mayor:
                nota_mayor = nota
            if nota < nota_menor:
                nota_menor = nota

    print(f"\n3. Nota mayor del grupo: {nota_mayor}")
    print(f"4. Nota menor del grupo: {nota_menor}")

# =============================================================================
# PARTE 10. RETO FINAL
# Ejercicio 10 — Sistema de estudiantes
# =============================================================================
def ejercicio_10():
    estudiantes = [
        ["Carlos", 20, 4.2],
        ["María", 19, 3.8],
        ["Juan", 21, 2.7]
    ]

    while True:
        print("\n=========================")
        print(" SISTEMA DE ESTUDIANTES ")
        print("=========================")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Mostrar promedio del grupo")
        print("5. Mostrar mayor nota")
        print("6. Mostrar menor nota")
        print("7. Mostrar aprobados")
        print("8. Salir")

        opcion = input("Seleccione una opción (1-8): ").strip()

        if opcion == "1":
            nombre = input("Nombre del estudiante: ").strip()
            try:
                edad = int(input("Edad: "))
                nota = float(input("Nota (0.0 - 5.0): "))
                if 0.0 <= nota <= 5.0:
                    estudiantes.append([nombre, edad, nota])
                    print(f"¡Estudiante {nombre} registrado exitosamente!")
                else:
                    print("Error: Nota fuera del rango permitido (0.0 a 5.0).")
            except ValueError:
                print("Error: Entrada numérica inválida.")

        elif opcion == "2":
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                print("\n--- LISTA DE ESTUDIANTES ---")
                for i, est in enumerate(estudiantes, 1):
                    print(f"{i}. Nombre: {est[0]} | Edad: {est[1]} | Nota: {est[2]}")

        elif opcion == "3":
            buscado = input("Ingrese el nombre del estudiante a buscar: ").strip()
            hallado = False
            for est in estudiantes:
                if est[0].lower() == buscado.lower():
                    print(f"Encontrado -> Nombre: {est[0]}, Edad: {est[1]}, Nota: {est[2]}")
                    hallado = True
                    break
            if not hallado:
                print(f"No se encontró ningún estudiante con el nombre '{buscado}'.")

        elif opcion == "4":
            if not estudiantes:
                print("No hay datos cargados.")
            else:
                suma = sum(est[2] for est in estudiantes)
                prom = suma / len(estudiantes)
                print(f"El promedio general del grupo es: {prom:.2f}")

        elif opcion == "5":
            if not estudiantes:
                print("No hay datos cargados.")
            else:
                mayor = max(estudiantes, key=lambda x: x[2])
                print(f"La nota más alta es {mayor[2]} (Estudiante: {mayor[0]})")

        elif opcion == "6":
            if not estudiantes:
                print("No hay datos cargados.")
            else:
                menor = min(estudiantes, key=lambda x: x[2])
                print(f"La nota más baja es {menor[2]} (Estudiante: {menor[0]})")

        elif opcion == "7":
            aprobados = [est for est in estudiantes if est[2] >= 3.0]
            print(f"\nTotal de aprobados: {len(aprobados)}")
            for est in aprobados:
                print(f"- {est[0]} (Nota: {est[2]})")

        elif opcion == "8":
            print("Saliendo del sistema de estudiantes...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
