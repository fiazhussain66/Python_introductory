import sympy as smp
from sympy import *

x = smp.symbols('x')

intigral = smp.integrate(8*x - smp.csc(x)**2, x)
c = -intigral.subs(x, smp.pi/2)-7
y = intigral+c
print(y)