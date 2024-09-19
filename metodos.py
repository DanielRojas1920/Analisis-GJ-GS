def det(matrix, nums=[1]): #Obtiene el determinante de una matriz
    total = 1
    for i in nums: total *= i
    if (len (matrix[0]) == 2): return total * (matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1])
    n = len(matrix[0])
    nums.append(matrix[0][0])
    matrix[0] = [i*(1/(nums[-1])) for i in matrix[0]]
    for count in range(1,n): matrix[count] = [-1*matrix[0][i]*matrix[count][0] + matrix[count][i] for i in range(1,n)]
    new_matrix = matrix[1:]
    return det(new_matrix, nums.copy())

def reorder_matrix(matrix):
    n = len(matrix[0])
    flag = False
    index_list= [0]*n
    for i in range(n): index_list[i] = [j for j in range(n) if((False in [(abs(matrix[j][z]) <= abs(matrix[j][i])) for z in range(n) if(z != i)]) != True)] + [-1]
    result = [i[0] for i in index_list]
    for i in range(n): 
        if (result.count(-1) == 0): break
        flag = True
        if((i in result) == False): result[result.index(-1)] = i
    return result, flag

def test_reorder_matrix(matrix):
    n = len(matrix[0])
    flag = False
    index_list= [0]*n #Buscar las filas donde se cumple el criterio de convergencia para cada variable
    for i in range(n): index_list[i] = [j for j in range(n) if((False in [(abs(matrix[j][z]) <= abs(matrix[j][i])) for z in range(n) if(z != i)]) != True)] + [-1]
    result = [i[0] for i in index_list]
    if (len(set(result)) == len(result)): return result, flag
    better_result = [-1]*n
    iter_index_list = [len(row)-1 for row in index_list]
    count_index_list = [0]*n
    index = -1
    while True: #Buscar combinaciones en caso de tener casos repetidos o casos con variables sin convergencia
        aux_result = [index_list[i][count_index_list[i]] for i in range(n)]
        print(aux_result)
        not_repeated = (len(set(aux_result)) == len(aux_result))
        if (aux_result.count(-1) == 0 and not_repeated): return aux_result, flag
        if (better_result.count(-1) > aux_result.count(-1) and not_repeated): better_result = aux_result.copy()
        if (sum(count_index_list) == sum(iter_index_list)): break
        while True:
            if (count_index_list[index] == iter_index_list[index]):
                count_index_list[index] = 0
                index -= 1
            else:
                count_index_list[index] += 1
                break
    flag = True
    for i in range(n): #Rellenar los -1 que quedaron con filas al azar
        if (better_result.count(-1) == 0): break
        if((i in result) == False): result[result.index(-1)] = i
    return result, flag


def gauss_seidel(matrix,b):
    iter = 0
    n = len(matrix[0])
    x = [0]*n
    xant = [0]*n
    err = [0]*n
    while (iter <= 100):
        for i in range(n): x[i] = sum([-1*x[j]*matrix[i][j] for j in range(n) if(j != i)] + [b[i]])/matrix[i][i]
        err = [abs((x[i]-xant[i])) for i in range(n)]
        for i in range(n): print(f"x{i},{iter} = {x[i]}; error = {err[i]}")
        err = [True if(i< 1e-3) else False for i in err]
        print("\n")
        if ((False in err) != True): break
        iter +=1
        xant = x.copy()
    if (iter > 100): print("Se supero el límite de iteraciones. El resultado puede no ser el correcto.")
    return x

def gauss_jordan(matrix, matrix_str = ""):
    n = len(matrix)
    for index in range(n):
        print(f"\niteración {index+1}\n")
        matrix[index]=[i*(1/(matrix[index][index])) for i in matrix[index]]
        for count in range(n): matrix[count] = [-1*matrix[index][i]*matrix[count][index] + matrix[count][i] for i in range(n+1)] if (index != count) else matrix[count]
        for row in matrix: print(f"[ {" ".join([str(round(i,2)) for i in row])} ]")
    return [b[-1] for b in matrix]


    

"""
a = [[0.1,7.0,-0.3],
    [3,-0.1,-0.2],
    [0.3,-0.2,-10],]
b = [-19.3, 7.85, 71.40]

a = [[1,2,],
    [4,5,],]
b = [3, 6]

index_list = test_reorder_matrix(a)


print([a[i] for i in index_list])

a = [[2,2,],
    [1,5,],]
b = [5, 3]

index_list = test_reorder_matrix(a)
"""


    
