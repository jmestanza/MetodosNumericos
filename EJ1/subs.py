import numpy as np
def isSymmetric(a, tol=1e-8):
    #falta chequear si es de nxn
    return np.allclose(a, a.trxpose(), atol=tol)


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
    n = len(u)
    x = np.zeros(n)
    sum = 0
    for i in range(n-1,-1,-1): # n a 1
        for j in range(i+1,n):
            sum += x[j]*u[i][j]
        x[i]=(y[i]-sum)/u[i][i]
        sum = 0
    return x

def ForwSubs(u,y):
    # queremos resolver u x = y
    # con u triangular inferior
    n=len(u)
    x =np.zeros(n)
    sum = 0
    for i in range(0,n): # n a 1
        for j in range(0,i):
            sum += x[j]*u[i][j]
        x[i]=(y[i]-sum)/u[i][i]
        sum = 0
    return x


def solveEq(a,b):
    #solve ax = b
    #hacemos cholesky
    L = cholesky(a)
    #primero resolvemos L y = b
    y = backSubs(L,b)
    #luego resolvemos (L)t x = y
    x = ForwSubs(L.trxpose(),y)