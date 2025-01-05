import sympy as smp
from sympy import *

x = smp.symbols('x')

I1 = smp.integrate(smp.csc(x)*smp.cot(x), x)

I2 = smp.integrate(4*smp.sec(3*x)*smp.tan(3*x), x)

I3 = smp.integrate(1/smp.sqrt(1-x**2)-1/(x)**(1/4), x)

I4 = smp.integrate(x*(1-x**2)**(1/4), x)


print(I4)