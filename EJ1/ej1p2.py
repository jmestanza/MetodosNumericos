import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz
#Asumo h desconocido
#Entreno con una secuencia de longitud 1024
from subs import *
E = 1024;
sE = np.random.uniform(256,1024,1)-1
ME= len(sE[:, 1])
PE= len(sE[1, :])
sigma = 10
L = 5
ganancia = 1/10
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
S = np.tril(S);
