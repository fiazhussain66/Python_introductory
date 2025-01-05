import sympy as smp
from sympy import *

n = smp.symbols('n')

exp1 = smp.Sum(6/4**n, (n, 0, smp.oo))
exp2 = smp.Sum(2**(n+1)/5**n, (n, 0, smp.oo))
exp3 = smp.Sum(smp.atan(n)/n**smp.Rational(11, 10), (n, 1, smp.oo))
exp4 = smp.Sum((1+smp.cos(n))/n**2, (n, 1, smp.oo))

print(exp4.n())