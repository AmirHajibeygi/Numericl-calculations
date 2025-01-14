clc;
clear;
disp("************In the name of God***********")
disp("please enter data to start calculation process...")
%Now we should write the function of this process
syms x y
g=@(x,y) (2/3)*(1+x/12)*1800-1200*y/(1200+600*x);
% we have IVP
x_zero=0;
y_zero=10;
h=0.01;
x_final=1;
while x_zero<x_final
    y_zero=y_zero+g(x_zero,y_zero)*h;
    x_zero=x_zero+h;
end
disp(y_zero)
%second part
%Runge kutta 2
%We have IVP
x_zero=0;
Y_zero=10;
while x_zero<x_final
    k1=g(x_zero,Y_zero);
    k2=g(x_zero+h/2,Y_zero+(h/2)*k1);
    Y_zero=Y_zero+g(x_zero+h/2,Y_zero+(h/2)*k1)*h;
    x_zero=x_zero+h;
end
disp(Y_zero)
%Runge kutta 3
%We have IVP
x_zero=0;
YY_zero=10;
while x_zero<x_final
    k1=g(x_zero,YY_zero);
    k2=g(x_zero+h/2,YY_zero+(h/2)*k1);
    k3=g(x_zero+h,YY_zero-k1*h+2*k2*h);
    YY_zero=YY_zero+(h/6)*(k1+4*k2+k3);
    x_zero=x_zero+h;
end
disp(YY_zero)
%%Runge kutta4
%We have IVP
x_zero=0;
YYY_zero=10;
while x_zero<x_final
    k1=g(x_zero,YYY_zero);
    k2=g(x_zero+h/2,YYY_zero+(h/2)*k1);
    k3=g(x_zero+h,YYY_zero-k1*h+2*k2*h);
    k4=g(x_zero+h,YYY_zero+k3*h);
    YYY_zero=YYY_zero+(h/6)*(k1+4*k2+k3);
    x_zero=x_zero+h;
end
disp(YYY_zero)
disp("According to calculations that we do we can conclude that Euler is the farthest answer:"+y_zero)
disp("And also we can conclude that Runge kutta2 is better than euler:"+Y_zero)
disp("And Runge kutta3 is better than Runge kutta2:"+YY_zero)
disp("And at last it is obvious that Runge kutta4 is the best form of calculation in there:"+YYY_zero)
disp("Thanks for your attention...")










