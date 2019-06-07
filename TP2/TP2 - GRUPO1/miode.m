
function [x t]=miode(f,x0,t0,tf,dtmax,tol,par)
  n = ceil((tf-t0)/dtmax);
  err = 1;
  
  while (err > tol)
    [x1 t1] = heun(f,x0,t0,tf,n,par); 
    [x2 t2] = heun(f,x0,t0,tf,n*2, par);
    err = max(abs(x1(tf)-x2(tf)));
    n = n + 1;
  end
  
  [x t] = heun(f,x0,t0,tf,n-1,par); 
