import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz
from subs import *
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
# plt.figure(1)
# plt.subplot(1,2,1)
# plt.imshow(a,cmap='gray',vmin=1,vmax=255)
# plt.subplot(1,2,2)
# plt.imshow(b,cmap='gray',vmin=1,vmax=255)
# plt.show()
#------------------------------
E = 1024;
sE = np.random.uniform(256,1024,1)-1

ME= len(sE[:, 1])
PE= len(sE[1, :])
h = ganancia*(1+np.random.randn(L))
z = np.zeros(ME-L)
HE=np.concatenate((h,z),axis=None)
H = toeplitz(h,np.zeros(ME))
rE= np.zeros((ME,PE))
NE= sigma*np.random.randn(ME,PE)
rE = HE.dot(sE) + NE
S = toeplitz(sE.transpose())
#S = S(:,1:L) # en octave dame todas las columnas de 1 a L
S= S[:,0:L+1] # en python 0:L+1 incluye hasta L
S = np.tril(S)
he=solveEq(S,rE)
#
z= np.zeros(M-L)
Heaux=np.concatenate((he,z),axis=None)
He= toeplitz(Heaux,np.zeros(M))
CN= (sigma**2)*np.eye(len(He))

sigmax= (1/256*(sum( np.power (((range(0,255))-np.mean(range(0,255))),2))))**(1/2)
mx= np.mean(range(0,255))*np.ones(M)
CX= (sigmax**2)*np.eye(len(He))

W = CX.dot(He.transpose())*np.linalg.inv((He.dot(CX)).dot(He.transpose)+CN)

d = np.zeros((M,P))
for k in range(1,P+1):
    #d(:,k) accede en octave a la columna k-esima
    d[:, k-1] = W.dot((r[:, k-1])-He.dot(mx))+ mx
d = d.astype(int)

plt.figure(2)
plt.subplot(1,3,1)
plt.imshow(a,cmap='gray',vmin=1,vmax=255)
plt.subplot(1,3,2)
plt.imshow(b,cmap='gray',vmin=1,vmax=255)
plt.subplot(1,3,2)
plt.imshow(d,cmap='gray',vmin=1,vmax=255)
plt.show()