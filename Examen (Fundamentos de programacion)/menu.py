


import random
import os
from funciones import *
workers = ["Juan Pérez", "Maria García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Fransisco Díaz", "Elena Fernández"]

print("[1] Asignar sueldos aleatorios")
print("[2] Clasificar sueldos")
print("[3] Ver estadísticas")
print("[4] Reporte de sueldos")
print("[5] Salir del programa")

select = str(input("Ingrese opción de menú: "))

while True:

    if select == "1":
        print()
        workers_salaries = []
        for i in workers:
            sueldo = random.randint(300_000, 2_500_000)
            workers_salaries.append({i:sueldo})
        os.system("cls")
        print("[1] Asignar sueldos aleatorios")
        print("[2] Clasificar sueldos")
        print("[3] Ver estadísticas")
        print("[4] Reporte de sueldos")
        print("[5] Salir del programa")
        print("Sueldos asignados: ")
        print(workers_salaries)
        select = str(input("Ingrese opción menú: "))

    if select == "2":
        print()
        salaries = []
        count_menores = 0
        menores = []
        for i in workers_salaries:
            for j in i:
                if i[j] < 800_000:
                    count_menores += 1
                    menores.append(i)
        count_between = 0
        between = []

        for i in workers_salaries:
            for j in i:
                if i[j] > 800_000 and i[j] < 2_000_000:
                    count_between += 1
                    between.append(i)
        
        count_mayores = 0
        mayores = []
        for i in workers_salaries:
            for j in i:
                if i[j] > 2_000_000:
                    count_mayores += 1
                    mayores.append(i)

        print(f"Sueldos menores a 800.000 Total {count_menores}" )
        print(menores)
        print(f"Sueldos entre 800.000 y 2.000.000 Total {count_between}" )
        print(between)
        print(f"Sueldos mayores a 2.000.000 Total {count_mayores}" )
        print(mayores)
        total = 0
        for i in workers_salaries:
            for j in i:
                total += i[j]
        print(f"TOTAL SUELDOS: ${total}")
        select = str(input("Ingrese opción menú: "))
    
    if select == "3":
        print()
        altos = []
        print("Sueldo más alto: ")
        print(max(mayor(mayores, altos)))

        bajos = []
        print("Sueldo más bajo: ")
        print(min(menor(menores, bajos)))

        average = []
        print("Promedio de sueldos: ")
        print(promedio(workers_salaries, average))
        select = str(input("Ingrese opción menú: "))
        
    if select == "4":
        print()
        print("Nombre empleado - Sueldo base - Descuento salud - Descuento AFP - Sueldo liquido")
        reports(workers_salaries)
        select = str(input("Ingrese opción menú: "))
    
    if select == "5":
        print()
        print("Haz finalizado menú")
        break






