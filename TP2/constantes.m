f0 = 0.05;
d_B = 0.7;
Cs = 5*10^(-3);
C = 0.0009127; %value reference (tablita)
k3 = 5.8 * 10^(-4);
k4 = 1.7 * 10^(-2);
k0 = 0.35;
K = 10;
klp = 3*10^6;
kop = 2*10^5;
r_L = 10^3;
k_P = 86;
S_P = 250;
k6 = 3;
k5 = 0.02;
P_ = I_P / k_P;
P0 = S_P / k_P;
Ps = k6 / k5;
pi_p = (P_ + P0)/(P_ + Ps);



D_R = 7*10^(-14);
D_B = f0 * d_B; 
k_B = 0.189;
D_C = 2.1*10^(-3);
D_A = 0.7;
R = 0.0007734;
B = 0.0007282;


pi_C = (C + f0 * Cs)/(C + Cs);
pi_L =(k3/k4)*((klp * pi_p * B)/(1 + (k3*K/k4) + (k1/(k2*k0))*((kop/pi_p)*R + I_0))) * (1 + (I_L/r_L));

