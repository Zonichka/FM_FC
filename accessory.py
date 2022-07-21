import numpy as np
import math
import copy


def change_lines(A, j):
    max_a = 0  # найдем максимальный модуль элемента и строку, содержащую данный элемент поменяем с j строкой
    n_a = 0  # номер строки, содержащий максимальный элемент j столбца

    for i in range(len(A)):
        if math.fabs(A[i][j]) >= max_a:
            max_a = A[i][j]
            n_a = i
    if j == 0:  # хотим поменять только первую строку, остальные не стоит
        A[j], A[n_a] = A[n_a], A[j]

    return max_a


def gauss(a, b):
    A = []
    for i in range(len(b)):
        A.append(a[i])
        A[i].append(b[i])  # матрица со столбцом b

    for j in range(len(A[0]) - 2):  # приводим матрицу к диагональному виду
        max_a = change_lines(A, j)
        for i in range(len(A) + 1):  # делим на старший коэффициент
            if max_a != 0:
                A[j][i] /= max_a
            else:
                print("По теореме Кронекера-Капелли, единственного решения у данной системы не существует.")
                return 0

        for k in range(len(A[j]) - 2 - j):  # прямой ход метода Гаусса
            a = -A[k + 1 + j][j]  # коэффициент перед первой строкой
            temp = copy.deepcopy(A[j])  # дубликат "рабочей" строки для сложения с ней низлежащих строк матрицы
            for i in range(j, len(A[j])):
                temp[i] *= a  # умножение на коэффициент для обнуления первого ненулевого элемента в низлежащих строках
                A[k + 1 + j][i] += temp[i]

    a = A[len(A) - 1][len(A) - 1]  # далее применение к последнему элементу матрицы b
    for i in range(4):
        A[len(A) - 1][i] /= a

    print("Results by Gauss method:")
    for i in range(len(A)):
        print("x_", i, " = ", A[i][len(A)], sep='')