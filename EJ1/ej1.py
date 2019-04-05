import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz
from utils import *
L = 5
ganancia = 1/10
h = ganancia*(1+np.random.randn(L))
sigma = 10
a = plt.imread(("lena512.bmp"))
M = len(a)
P = len(a[0])
z = np.zeros(M-L)
h = np.transpose(h)
h=np.concatenate((h,z),axis=None)
H = toeplitz(h,np.zeros(M))
r = np.zeros((M,P))
N = sigma*np.random.randn(M,P)
s = a
r = H.dot(s) + N
b =(r.astype(int))
# plt.figure(1)
# plt.subplot(1,2,1)
# plt.imshow(a,cmap='gray',vmin=1,vmax=255)
# plt.subplot(1,2,2)
# plt.imshow(b,cmap='gray',vmin=1,vmax=255)
# plt.show()
#------------------------------
E = 1024
sE = np.random.uniform(0,256,(1024,1))

ME= len(sE)#cols
PE= len(sE[0]) # fils
h = ganancia*(1+np.random.randn(L))
z = np.zeros(ME-L)
HE=np.concatenate((h,z),axis=None)
H = toeplitz(h,np.zeros(ME))
rE= np.zeros((ME,PE))
NE= sigma*np.random.randn(ME,PE)
NE = np.concatenate(NE, axis=0 )
sE = np.concatenate(sE, axis=0 )
rE = HE.dot(sE) + NE
rE = rE.transpose()
S = toeplitz(sE.transpose())
#S = S(:,1:L) # en octave dame todas las columnas de 1 a L
S= S[:,0:L+1] # en python 0:L+1 incluye hasta L
S = np.tril(S)
# #print(HE.dot(sE))
# multiplicamos ambos miembros por izquierda para obtener una matriz
# simetrica y aplicar cholesky
Saux = (S.transpose()).dot(S)
rEaux = (S.transpose()).dot(rE)
he=solveEq(Saux,rEaux)

z= np.zeros(M-L-1)
Heaux=np.concatenate((he,z),axis=None)
He= toeplitz(Heaux,np.zeros(M)) #con M He es de 512x512

CN= (sigma**2)*np.eye(len(He))


sigmax= (1/256*(sum( np.power (((range(0,255))-np.mean(range(0,255))),2))))**(1/2)
mx= np.mean(range(0,255))*np.ones(M)
CX= (sigmax**2)*np.eye(len(He))
aux = (He.dot(CX)).dot(He.transpose())+CN
invaux = np.linalg.inv(aux)
mult1 = CX.dot(He.transpose())
mult2 = mult1.dot(invaux)
W = mult2
# #W = CX.dot(He.transpose()).dot(np.linalg.inv((He.dot(CX)).dot(He.transpose)+CN))
# # M = M+1
# # P = P+1
d = np.zeros((M,P))
#mx es un array de 1x512
example = (r[:, 0])-He.dot(mx)

for k in range(0,P):
    #d(:,k) accede en octave a la columna k-esima
    d[:, k] = W.dot((r[:, k])-He.dot(mx)) + mx
d = d.astype(int)

plt.figure(2)
plt.subplot(1,3,1)
plt.imshow(a,cmap='gray',vmin=1,vmax=255)
plt.subplot(1,3,2)
plt.imshow(b,cmap='gray',vmin=1,vmax=255)
plt.subplot(1,3,3)
plt.imshow(d,cmap='gray',vmin=1,vmax=255)
plt.show()