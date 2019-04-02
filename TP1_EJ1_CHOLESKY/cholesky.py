import numpy as np
import matplotlib.pyplot as plt
#from scipy.linalg import toeplitz

print("hello world")

def cholesky(a):
    print(a)
    print(a[0][1])
    print(" chau")
    return a

def isSimetric(a):
    # A.transpose()
    print("ADENTRO a PRINCIPIO: ", a)
    at=a
    print("ADENTRO a PRINCIPIO 1: ", a)
    # iterate through rows
    for i in range(len(a)):
        # iterate through columns
        for j in range(len(a[0])):
            at[j][i] = a[i][j]
            j=j+1
        i=i+1

    print("ADENTRO a: ", a)
    print("ADENTRO at: ", at)
    if at == a:
        return True
    else:
        return False

#------------------------------------------------------
# Program to transpose a matrix using nested loop

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]
# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
#------------------------------------------------------

aa=[[2, 3, 2],
   [3, 5, 3],
   [2, 3, 3]]

cc=np.matrix('2 3 2; 3 5 3; 2 3 3')

a=[[0, 0, 0],
   [0, 0, 0],
   [0, 0, 0]]

bb=[[0, 1, 2],
   [3, 4, 5],
   [6, 7, 8]]

a=cholesky(aa)
print("bb=", bb)
print("ES aa SIMETRICA? ", isSimetric(bb))
#isTransposeOf(bb)