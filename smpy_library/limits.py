import sympy as smp
from sympy import *

x, y = smp.symbols('x y')

exp1 = smp.limit(smp.sin(x/2 + smp.sin(x)), x, smp.pi)
exp2 = smp.limit(2*smp.exp(1/x) / (smp.exp(1/x)+1), x, 0, dir='+')
exp3 = smp.limit(2*smp.exp(1/x) / (smp.exp(1/x)+1), x, 0, dir='-')
exp4 = smp.limit((smp.cos(x) - 1)/x, x, smp.oo)


print(exp1, exp2, exp3, exp4)