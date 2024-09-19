import os
from metodos import *

def menu():
    n=3
    matrix = [[0.1,7.0,-0.3],
              [3,-0.1,-0.2],
              [0.3,-0.2,-10],]
    index_list = []
    flag = False
    
    b = [-19.3, 7.85, 71.40]

    select = 0

    while select != 4:
        os.system('cls')
        print("\nSolucionador de sistemas de ecuaciones lineales\n\n")
        print("1. Cambiar matriz aumentada")
        print("2. Método de Gauss-Jordan")
        print("3. Método de Gauss-Seidel")
        print("4. Salir")

        print("\nMatriz aumentada actual:\n")
        for i in range(n): print(f"[ {" ".join([str(round(num,2)) for num in matrix[i]] + [str(round(b[i], 2))])} ]")

        try: #try except para validar el input
            select = int(input("\nIntroduzca la opción a realizar: "))
            if (select <= 0 or select >= 5):
                print("Opción inválida")
                os.system("pause")
        except Exception as err:
            if (err == KeyboardInterrupt): raise KeyboardInterrupt #Permite usar ctrl+c para terminar en seco el programa
            print("Opción inválida")
            os.system("pause")
            select = 0

        while (select == 1): #Cambiar matriz
            os.system("cls")
            print("matriz actual: ")
            for i in matrix: print(i)
            try: 
                n_aux = int(input("\nintroduzca el valor del alto y el ancho de la matriz (n): "))
                aux_matrix = []
                aux_b = []
                for i in range(n_aux): 
                    row = (input(f"Introduzca los coeficientes de la matriz aumentada de la fila {i+1} espaciados: ")).split(" ")
                    row = [float(i) for i in row]
                    if (len(row) == n_aux+1): 
                        aux_matrix.append(row[:-1])
                        aux_b.append(row[-1])
                    else: raise ValueError("Error")
                select = 0 if (str(input("\nDeseas continuar? (y: sí): ")).lower() == 'y') else -1 #Si se introduce y, se guarda la función ingresada
                if (select == 0): 
                    matrix = aux_matrix.copy()
                    b = aux_b.copy()
                    n = n_aux 
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print("Valor inválido")
                os.system("pause")
        
        while (select == 2): #Método Gauss-Jordan
            os.system("cls")
            print("Método Gauss-Jordan")
            aumented_matrix = [matrix[i] + [b[i]] for i in range(n)]
            print("\n\n",gauss_jordan(aumented_matrix))
            os.system("pause")
            select = 0
        
        while (select == 3): #Método Gauss-Seidel
            os.system("cls")
            try:
                print("Método Gauss-Seidel\n")
                if (round(det(matrix.copy(), []), 5) == 0): raise ValueError("Error")
                index_list, flag= reorder_matrix(matrix)
                print(gauss_seidel([matrix[i] for i in index_list], [b[i] for i in index_list]))
                if (flag): print("La matriz no cumple el criterio de convergencia. La solución puede no ser la correcta. \n")
                select = 0
                os.system("pause")
            except Exception as err:
                if (err == KeyboardInterrupt): raise KeyboardInterrupt
                print("La matriz no tiene soluciones únicas")
                select = 0
                os.system("pause")



menu() #Ejecuta el programa