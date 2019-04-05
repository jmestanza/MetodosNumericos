from utils import *
from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
from scipy.linalg import toeplitz
from numpy.linalg import inv
sigma = 0.1
L = 5
ganancia = 1/10
h = ganancia*(1+randn(1,L))
a = imread(("lena512.bmp"))
M = len(a[:, 0])
P = len(a[0, :])
z = np.zeros(M-L)
H = toeplitz(np.concatenate((h,z),axis=None),zeros(M))
r = zeros((M,P))
N = sigma*randn(M,P)
s = a.astype(float64)
r = matmul(H,s) + N
b = uint8(r)
# #------------------------------
L = 5
ganancia = 1/10
sigma = 0.1
E = 1024
sE = np.random.uniform(1,255,size=(E,1))-1
ME= len(sE[:, 0]) #cols
PE= len(sE[0, :]) # fils
#ajusto sE para el producto
z = np.zeros(ME-L)
HE= toeplitz(concatenate((h,z),axis=None),zeros(ME))
rE= zeros((ME,PE))
NE= sigma*randn(ME,PE)
#NE = zeros((ME,PE))
rE = matmul(HE,sE) + NE
S = toeplitz(sE.transpose())
#S = S(:,1:L) # en octave dame todas las columnas de 1 a L
S= S[:,0:L+1] # en python 0:L+1 incluye hasta L
S = tril(S)
# multiplicamos ambos miembros por izquierda para obtener una matriz
# simetrica y aplicar cholesky
St = S.transpose()

he=solveEq(matmul(St,S),matmul(St,rE))
z= zeros(M-L-1)
He= toeplitz(concatenate((he,z),axis=None),zeros(M))

CN= (sigma**2)*eye(len(He))

sigmax= (1/256*(sum(np.power (((range(0,255))-mean(range(0,255))),2))))**(1/2)
mx= mean(range(0,255))*ones(M)
CX= (sigmax**2)*eye(len(He))
aux = matmul(matmul(He,CX),He.transpose())+CN
W = matmul(matmul(CX,He.transpose()),inv(aux))
#----------------------------------------------------------

d = zeros((M,P))
for k in range(0,P):
    #d(:,k) accede en octave a la columna k-esima
    d[:, k] = W.dot((r[:, k])-He.dot(mx)) + mx

d = uint8(d)
figure(2)
subplot(1,3,1)
imshow(a,cmap='gray',vmin=0,vmax=255)
subplot(1,3,2)
imshow(b,cmap='gray',vmin=0,vmax=255)
subplot(1,3,3)
imshow(d,cmap='gray',vmin=0,vmax=255)
show()