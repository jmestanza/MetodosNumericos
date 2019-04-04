from subs import *
import numpy as np
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
b = np.array([2,3,4])

x1=np.linalg.solve(a,b)
x2=solveEq(a,b)
print(x1)
print(x2)