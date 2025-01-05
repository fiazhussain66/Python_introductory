import sympy as smp
from sympy import *

x = smp.symbols('x')
t = smp.symbols('t')

sol_1 = smp.integrate(smp.exp(x) / smp.sqrt(smp.exp(2*x)+9), (x, 0, smp.log(4)))

sol_2 = smp.integrate(x**10*smp.exp(x), (x, 1, t))

sol_3 = smp.integrate(16*smp.atan(x)/(1+x**2), (x, 0,smp.oo))

print(sol_3)