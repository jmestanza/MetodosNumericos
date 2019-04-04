import numpy as np
import matplotlib.pyplot as plt
import math
#from scipy.linalg import toeplitz


def isSymmetric(a, tol=1e-8):
    #falta chequear si es de nxn
    return np.allclose(a, a.transpose(), atol=tol)


def isEqual(a,b, tol=1e-8):
    return np.allclose(a, b, atol=tol)


def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)


def cholesky(a):

    if isSymmetric(a) and is_pos_def(a):
        w = len(a)
        l = np.zeros((w,w)) # matriz de wxw
        #sum1 y sum2 son las sumatorias de las formulas
        sum1 = 0
        sum2 = 0
        #j es columna,i es fila
        #como lo primero que termina una iteracion en el proceso son las filas
        #entonces deben estar adentro del for de las columnas
        for j in range(0, w):
            for i in range(j, w):
                if i == j: #formula para cuando i vale j
                    for k in range(0, i):
                        sum1 += (l[i][k]) ** 2
                    l[i][i] = (a[i][i] - sum1) ** (1 / 2)
                    sum1 = 0
                else:     #formula para cuando i distinto j
                    for k in range(0, j):
                        sum2 += l[i][k]*l[j][k]
                    l[i][j] = (a[i][j]-sum2)/(l[j][j])
                    sum2 = 0
        return l
    else:
        return None

def backSubs(u,y):
    # queremos resolver u x = y
    # con a triangular superior
    n=len(a)
    ans =np.zeros(n)
    sum = 0
    for i in range(n-1,-1,-1): # n a 1
        for j in range(i+1,n):
            sum += x[j]*u[i][j]
        ans[i]=(y[i]-sum)/u[i][i]
        sum = 0
    return ans

def backSubs(u,y):
    # queremos resolver u x = y
    # con a triangular superior
    n = len(a)
    ans = np.zeros(n)
    sum = 0
    for i in range(n-1,-1,-1): # n a 1
        for j in range(i+1,n):
            sum += x[j]*u[i][j]
        ans[i]=(y[i]-sum)/u[i][i]
        sum = 0
    return ans

def ForwSubs(u,y):
    # queremos resolver u x = y
    # con u triangular inferior
    n=len(a)
    ans =np.zeros(n)
    sum = 0
    for i in range(0,n): # n a 1
        for j in range(0,i):
            sum += x[j]*u[i][j]
        ans[i]=(y[i]-sum)/u[i][i]
        sum = 0
    return ans


j = np.array([[25,15,-5,-10],
              [15,10, 1,-7],
              [-5,1 ,21, 4],
              [-10,-7,4,18]])

# c = cholesky(j)
# print("Cholesky obtenida:\n",c)
# L = np.linalg.cholesky(j)
# print("El resultado al que tengo que llegar es:\n",L)
# ans = "no"
# if isEqual(c,L):
#     ans = "sí"
# else:
#     ans = "no"
# print("el resultado "+ans+" es igual!!")
a = np.array([3,1, 1,2])
c = cholesky(j)

# x = np.linalg.solve(c.transpose(), b)
# x2= backSubs(c.transpose(),b)
x = np.linalg.solve(c, a)
x2= ForwSubs(c,a)
print(c)
print(x)
print(x2)