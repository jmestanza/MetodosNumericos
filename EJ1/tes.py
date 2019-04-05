from numpy import *
from numpy.random import *
from matplotlib.pyplot import *
from scipy.linalg import toeplitz
L = 5;
ganancia = 1/10;
h = ganancia*(1+randn(L,1));
sigma = 0.1;
a = imread('lena512.bmp');
M = size(a,1);
P = size(a,0);
aux = concatenate((h,zeros(M-L)),axis=None)
H = toeplitz(aux,zeros(M));
r = zeros((M,P));
N = sigma*randn(M,P);
s = a.astype(float64)
r = H.dot(s) + N;
b = uint8(r);
figure(1)
subplot(1,2,1)
imshow(a,cmap='gray',vmin=0,vmax=255)
subplot(1,2,2)
imshow(b,cmap='gray',vmin=0,vmax=255)
show()