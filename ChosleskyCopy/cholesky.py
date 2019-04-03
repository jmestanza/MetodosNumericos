import numpy as np
import matplotlib.pyplot as plt
import math
#from scipy.linalg import toeplitz

def isSymmetric(a, tol=1e-8):
    #falta chequear si es de nxn
    return np.allclose(a, a.transpose(), atol=tol)
def cholesky(a):
    if isSymmetric(a):
        w = len(a)
        g = np.zeros((w,w))
        for j in range(w):
            sum = 0
            for k in range(j - 1):
                sum += ((g[j][k]) ** 2)
            g[j][j] = math.sqrt(a[j][j] - sum)
            j = j + 1
        #-------------------------------
            # iterate through rows
        for i in range(w):
            # iterate through columns
            for j in range(i-1):
                sum = 0
                for k in range(j-1):
                    sum += (g[i][k] * g[j][k])
                g[i][j] = (a[i][j] - sum) / (g[j][j])
                j = j + 1               #PUEDE SER QUE ESTO NO HAGA FALTA?
            i = i + 1                   #PUEDE SER QUE ESTO NO HAGA FALTA?

        gt = g.transpose()
        matArr = [g, gt]
        return (matArr)
    else:
        return [False, False]

#------------------------------------------------------

#------------------------------------------------------

aa = np.array([[2, 3, 2],
               [3, 5, 3],
               [2, 3, 3]])

a = np.array([[0, 0, 0],
              [0, 0, 0]])

b = np.array([[0, 1, 2],
              [3, 4, 5]])

bb = np.array([[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]])

#print(isSymmetric(aa))

bb = np.array([[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]])

c = cholesky(aa)
print("La primera matriz:\n",c[0])
print("La segunda matriz:\n",c[1])
#print("mat transpuesta:\n", b.transpose())
#print("matProduct:\n", aa.dot(bb))
