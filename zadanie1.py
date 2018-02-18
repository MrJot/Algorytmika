import math
import numpy as np
print("Program rozwiazujacy uklad rownan w postaci:\nAx + By = C\nDx + Ey = F")
A=float(input("Podaj A= "))
B=float(input("Podaj B= "))
C=float(input("Podaj C= "))
D=float(input("Podaj D= "))
E=float(input("Podaj E= "))
F=float(input("Podaj F= "))

a = np.array([[A, B],[D,E]])
a_uzup=np.array([[A,B,C],[D,E,F]])
print(np.linalg.matrix_rank(a))
print(np.linalg.matrix_rank(a_uzup))
b = np.array([C, F])
if np.linalg.matrix_rank(a)==np.linalg.matrix_rank(a_uzup)==2:
    print("Równanie ma jedno rozwiązanie")
    sol=(np.linalg.solve(a,b))
    print('x = %5.2f , y = %5.2f' % (sol[0], sol[1]))
elif np.linalg.matrix_rank(a)==np.linalg.matrix_rank(a_uzup)<2:
    print("Układ ma nieskończenie wiele rozwiązań")
else:
    print("Układ równań jest układem sprzecznym")
