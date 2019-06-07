
function [x t]=heun(f,x0,t0,tf,n,par)
    h=(tf-t0)/n;
    t=linspace(t0,tf,n);
    x(1,:)=x0;
    for i=1:n-1
        k1(i,:)=f(t(i),x(i,:), par);
        k2(i,:)=f(t(i)+h,x(i,:)+k1(i,:), par);
        x(i+1,:)=x(i,:)+(h/2)*(k1(i,:)+k2(i,:));
    end
    