from subs import *
import numpy as np
a = np.array([[4,12,-16],
              [12,37,-43],
              [-16,-43,98]])
b = np.array([2,3,4])

x1=np.linalg.solve(a,b)
x2=solveEq(a,b)
print(x1)
print(x2)