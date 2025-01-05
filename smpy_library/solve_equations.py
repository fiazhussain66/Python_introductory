import sympy as smp
from sympy import *

x, y = smp.symbols('x y', real = True, postive = True)

z = x**2+y
sol = smp.solve(z, x) # solve comand in sympy library

z1 = (x**2 - 7*x +10)**2

sol1 = smp.solve(z1, x)

# sympy factor comand

sol2 = smp.factor(z1, x)

# sympy expand comand

sol3 = smp.expand(z1, x)

print(sol3)