
f=@(t,y,p)[t];
par = 0

[x,t] = miode(f, 4, -2, 2,1,0.01,par)

plot(t,x)
