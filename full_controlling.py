import numpy as np
import sympy as sym
from sympy.matrices import Matrix
from fund_matrix import Y


t = sym.var('t')


def checking_of_FC(P, Q, T):
      S0 = Q
      S = S0.T
      for i in range(P.shape[1]):
            Si = S0.diff(t).T
            Si -= (P * S0).T
            S = Matrix([S, Si])
            S0 = Si.T

      b = list()  # возможные значения t, при которых ранг матрицы может быть наибольшим
      b.append(np.linspace(0, 10, T))
      tau = sym.pi
      while tau < T:
            i = 1
            tau = sym.pi * i
            b.append(tau)
            i += 1

      for tau in b:
            if S.T.rank().sym.subs(t, tau) == P.shape[1]:
                  return True

      return False


def controlling_pair_of_points(P, Q, f, T, x0, x1):
      B = sym.simplify(Y(P).inv() * Q)
      print(B)
      A = sym.integrate((sym.simplify(B * B.T)), (t, 0, T))
      print(A)

      teta = Y(P).inv().subs('t', T) * x1 - x0 - sym.integrate((sym.simplify(Y(P).inv() * f)), (t, 0, T))

      A_teta = Matrix([A, teta])

      if A.rank() == A_teta.rank():
            return 1
      else:
            return 0


def full_controlling(P, Q, f, T, x0, x1):
      if checking_of_FC(P, Q, T) == False:
            print("System is not FC")
            if controlling_pair_of_points(P, Q, f, T, x0, x1):
                  print("Pair of points is can be controlled")
            else:
                  print("Pair of points can not be controlled")
            return 0

      B = sym.simplify(Y(P).inv() * Q)
      print(B)
      A = sym.integrate((sym.simplify(B * B.T)), (t, 0, T))
      print(A)

      teta = Y(P).inv().subs('t', T) * x1 - x0 - sym.integrate((sym.simplify(Y(P).inv() * f)), (t, 0, T))
      print(teta)
      C = A.inv() * teta
      print(C)


print("Program of search FC")
P = Matrix([[0, 1, 1], [-1, 0, 1], [0, 0, 0]])
Q = Matrix([1, 0, 1])
f = Matrix([sym.sin(t), sym.cos(t), 1])
x0 = Matrix([1, 0, 0])
x1 = Matrix([0, 0, 0])
T = sym.pi

print(full_controlling(P, Q, f, T, x0, x1))

P = Matrix([[1, 0], [1, 1]])
Q = Matrix([0, 1])
f = Matrix([0, 0])
x0 = Matrix([0, 0])
x1 = Matrix([1, 4])
T = 1

print(full_controlling(P, Q, f, T, x0, x1))

P = Matrix([[2, 1], [-1, 2]])
Q = Matrix([sym.exp(2*t), 0])
f = Matrix([0, sym.exp(2*t)*sym.sin(t)])
x0 = Matrix([1, 1])
x1 = Matrix([0, 0])
T = 2*sym.pi

print(full_controlling(P, Q, f, T, x0, x1))
