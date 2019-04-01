import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz

L = 5
ganancia = 1/10
h = ganancia*(1+np.random.randn(L))
sigma = 10
a = plt.imread(("lena512.bmp"))
M = len(a[:, 1])
P = len(a[1, :])
z = np.zeros(M-L)
h = np.transpose(h)
h=np.concatenate((h,z),axis=None)
H = toeplitz(h,np.zeros(M))
r = np.zeros((M,P))
N = sigma*np.random.randn(M,P)
s = a
r = H.dot(s) + N
b =(r.astype(int));
plt.figure(1)
plt.subplot(1,2,1)
plt.imshow(a)
plt.subplot(1,2,2)
plt.imshow(b)
plt.show()