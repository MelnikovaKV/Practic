import random

x = int(input('Введите количество строк в матрице'))
y = int(input('Введите количество столбцов в матрице'))

matrix_1 = [[random.randint(1, 50) for i in range(y)] for i in range (x)]
matrix_2 = [[random.randint(-50, 50) for i in range(y)] for i in range (x)]

print('Первая матрица')
for i in range (x):
        print(matrix_1[i])

print('Вторая матрица') 
for i in range (x):
    print(matrix_2[i])

matrix_3 = [[matrix_1[i][j] + matrix_2[i][j] for j in range (y)] for i in range(x)]
print('Сложение элементов матриц')
for i in matrix_3:
    print(i)

matrix_4 = [[matrix_1[i][j] - matrix_2[i][j] for j in range (y)] for i in range(x)]
print('Вычитание элементов матриц')
for i in matrix_4:
    print(i)  

matrix_5 = [[matrix_1[i][j] * matrix_2[i][j] for j in range (y)] for i in range(x)]
print('Умножение элементов матриц')
for i in matrix_5:
    print(i)  