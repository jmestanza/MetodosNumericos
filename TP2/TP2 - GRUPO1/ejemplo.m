f=@(t,y,p) 2*t;

[x t] = miode(f, 1, -2, 2, 1, 10^-1,'a');

plot(t,x)