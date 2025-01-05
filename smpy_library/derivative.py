import sympy as smp
from sympy import *

x = smp.symbols('x')
f,g = smp.symbols('f g', cls = smp.Function)

f = f(x)
g = g(x+f)

exp1 = ((1-smp.sin(x)) / (1-smp.cos(x)))**2
exp2 = (smp.log(x,5))**x/2

dfdx_1 = smp.diff(exp1, x)
dfdx_2 = smp.diff(exp2, x)
dfdx_3 = smp.diff(g, x)

print(dfdx_3)