import numpy as np
import matplotlib.pyplot as plt
import math
#from scipy.linalg import toeplitz

#print("hello world")

def transpose(a):
    w,h = len(a),len(a[0])
    at = [[0 for x in range(w)] for y in range(h)]
    # iterate through rows
    for i in range(len(a)):
        # iterate through columns
        for j in range(len(a[0])):
            at[j][i] = a[i][j]
            j=j+1               #PUEDE SER QUE ESTO NO HAGA FALTA?
        i=i+1                   #PUEDE SER QUE ESTO NO HAGA FALTA?
    return at

def isSymmetric(a):
    #print("MATRIZ RECIBIDA: ", a)
    if len(a) != len(a[0]):
        return False

    at = transpose(a)
    print("AL FINAL a: ", a)
    print("AL FINAL at: ", at)

    if at == a:
        return True
    else:
        return False


def cholesky(a):
    if isSymmetric(a):
        w = len(a)
        g = [[0 for x in range(w)] for y in range(w)]
        #-------------------------------
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
        gt = transpose(g)
        matArr = [g, gt]
        return (matArr)
    else:
        return [False, False]

#------------------------------------------------------

#------------------------------------------------------

aa = [[2, 3, 2],
    [3, 5, 3],
    [2, 3, 3]]

#cc=np.matrix('2 3 2; 3 5 3; 2 3 3')

a = [[0, 0, 0],
    [0, 0, 0]]

b = [[0, 1, 2],
    [3, 4, 5]]

bb = [[0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]]

#a=cholesky(aa)
#print("bb=", bb)
print("mat transpuesta: ", transpose(b))
print("Is matrix simetric?:", isSymmetric(bb))
gygt = cholesky(aa)
print ("g= ", gygt[0])
print ("gt= ", gygt[1])
g = gygt[0]
gt = gygt[1]
print ("g= ", g)
print ("gt= ", gt)

#isTransposeOf(bb)