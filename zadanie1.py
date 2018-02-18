import math
import numpy as np
print("Program rozwiazujacy ukaad rawnaa w postaci:\nAx + By = C\nDx + Ey = F")
A=input("Podaj A= ")
B=input("Podaj B= ")
C=input("Podaj C= ")
D=input("Podaj D= ")
E=input("Podaj E= ")
F=input("Podaj F= ")

a = np.array([[1, 1],[2,4]])
b = np.array([35, 94])

print(np.linalg.solve(a,b))

