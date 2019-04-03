import numpy as np
import matplotlib.pyplot as plt
import math
#from scipy.linalg import toeplitz

def isSymmetric(a, tol=1e-8):
    #falta chequear si es de nxn
    return np.allclose(a, a.transpose(), atol=tol)
def isEqual(a,b, tol=1e-8):
    return np.allclose(a, b, atol=tol)


def cholesky(a):
    if isSymmetric(a):
        w = len(a)
        n = w + 1
        l = np.zeros((n,n))
        sum1 = 0
        sum2= 0
        #p es i fila
        #q es j columna
        for j in range(1, n):  # j es columna
            for i in range(j, n):  # esto esta bien
                #esto esta bien
                #----------------------------
                if i==j:
                    for k in range(1,i):
                        sum1 += (l[i][k]) ** 2
                    l[i][i] = (a[i - 1][i - 1] - sum1) ** (1 / 2)
                    sum1 = 0
                else:
                    for k in range(1,j):
                        sum2+=l[i][k]*l[j][k]
                    l[i][j] = (a[i-1][j-1]-sum2)/(l[j][j])
                    sum2 = 0

        #estas borran los 0s sin utilizar para que sea adecuada la matriz
        ans = l.copy()
        ans = np.delete(ans,0,1)
        ans = np.delete(ans,0,0)
        return ans
    else:
        return None

#------------------------------------------------------

j = np.array([[25,15,-5,-10],
              [15,10, 1,-7],
              [-5,1 ,21, 4],
              [-10,-7,4,18]])

c = cholesky(j)
print("Cholesky obtenida:\n",c)
L = np.linalg.cholesky(j)
print("El resultado al que tengo que llegar es:\n",L)
ans = "no"
if isEqual(c,L):
    ans = "sí"
else:
    ans = "no"
print("el resultado "+ans+" es igual!!")

