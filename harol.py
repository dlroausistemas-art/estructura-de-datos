Cant=3
i=0
j=0
notas=[[0]*Cant for i in range(Cant)]
for i in range(Cant):
    for j in range(Cant):
        notas[i][j] = float(input("Ingrese la nota de estudiante: "))
print (notas)