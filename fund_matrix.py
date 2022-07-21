import math
import numpy as np
from numpy import linalg as lg
import sympy as sym
from sympy.matrices import Matrix


# Ввод матрицы с клавиатуры
print("Program of search FM")
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
print("Enter the entries in a single line (separated by space): ")
entries = list(map(int, input().split()))
P = np.array(entries).reshape(R, C)
P = Matrix(P)
print(P)
t = sym.Symbol('t')


def polinomial_system(P):
    # Собственные числа и векторы матрицы A
    count_values = P.eigenvals()
    phi = Matrix()

    # Здесь составляются строки для системы полиномов. Максимальная кратность собственного числа - 3.
    # Комплексно-сопряженная пара может быть кратности только 1.
    # else -> continue необходим, потому что строки я составляю для i>=0 и для всей пары.
    for value, n in count_values.items():
        if n == 1 and sym.im(value) > 0:
            phi_i = Matrix([[1, sym.re(value), -sym.im(value)**2, sym.exp(sym.re(value) * t) * sym.cos(sym.im(value) * t)],
                           [0, sym.im(value), sym.re(value)**2, sym.exp(sym.re(value) * t) * sym.sin(sym.im(value) * t)]])
        elif n == 3:
            phi_i = Matrix([[1, value, value ** 2, sym.exp(value * t)],
                           [0, 1, 2 * value, t * sym.exp(value * t)],
                           [0, 0, 2, t**2 / 2 * sym.exp(value * t)]])
        elif n == 2:
            phi_i = Matrix([[1, value, value ** 2, sym.exp(value * t)],
                           [0, 1, 2 * value, t * sym.exp(value * t)]])
        elif n == 1 and sym.im(value) == 0:
            phi_i = Matrix([[1, value, value ** 2, sym.exp(value * t)]])
        else:
            continue
        phi = Matrix([phi, phi_i])
    
    return phi


# linsolve принимает 3 символа, для которых и систему, состоящую из матрицы коэффициентов A и вектора решений b.
# Так как linsolve дает FiniteSet, распаковывать его нужно итеративно.
def phi(P):
    phi = list()

    if len(P) == 9:
        x0, x1, x2 = sym.symbols('x0 x1 x2')
        system = A, b = polinomial_system(P)[:, :-1], polinomial_system(P)[:, -1]
        ans = sym.linsolve(system, x0, x1, x2)
        (phi0, phi1, phi2) = next(iter(ans))
        phi = [phi0, phi1, phi2]

    elif len(P) == 4:
        x0, x1 = sym.symbols('x0 x1')
        system = A, b = polinomial_system(P)[:, :-1], polinomial_system(P)[:, -1]
        ans = sym.linsolve(system, x0, x1)
        (phi0, phi1) = next(iter(ans))
        phi = [phi0, phi1]

    return phi


def Y(A):
    ans = phi(A)
    p = A**2
    y = Matrix()
# Так как при умножении на символьное выражение происходит несовместимость типов, матрица-полином
# p(A) = phi0*E + phi1*A + ... + phi(n-1)*A^(n-1) умножается именно так и только для матрицы размерности 2 и 3.
    if len(p) == 9:
        yi = Matrix([ans[0] + ans[1] * A.row(0)[0] + ans[2] * p.row(0)[0],
                     ans[1] * A.row(0)[1] + ans[2] * p.row(0)[1],
                     ans[1] * A.row(0)[2] + ans[2] * p.row(0)[2]])
        yi = yi.T
        y = Matrix(yi)

        for i in range(1, 3):
            for j in range(3):
                if i == j:
                    yj = Matrix([ans[0] + ans[1] * A.row(i)[j] + ans[2] * p.row(i)[j]])
                else:
                    yj = Matrix([ans[1] * A.row(i)[j] + ans[2] * p.row(i)[j]])
                if j == 0:
                    yi = Matrix(yj)
                else:
                    yi = Matrix([yi, yj])
            yi = yi.T
            y = Matrix([y, yi])

    elif len(A) == 4:
        yi = Matrix([ans[0] + ans[1] * A.row(0)[0],
                     ans[1] * A.row(0)[1]])
        yi = yi.T
        y = Matrix(yi)

        for i in range(1, 2):
            for j in range(2):
                if i == j:
                    yj = Matrix([ans[0] + ans[1] * A.row(i)[j]])
                else:
                    yj = Matrix([ans[1] * A.row(i)[j]])
                if j == 0:
                    yi = Matrix(yj)
                else:
                    yi = Matrix([yi, yj])
            yi = yi.T
            y = Matrix([y, yi])

    return y


print(Y(P))
