import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import scienceplots

plt.style.use(['science', 'notebook', 'grid'])


def dfdt(f, t,  a, r, b, c):
    S = f[0]
    E = f[1]
    I = f[2]
    R = f[3]
    return[
        -a*S*E -r*S+r*R,
        a*S*E-(b+r)*E,
        (2*b - c)*E -r*I,
        (c-b)*E-2*r*R
    ] 
    
times = np.linspace(0, 1000, 1000)

a = 0.00003
b = 0.02
c = 0.03
r = 0.01

S0, E0, I0, R0 = 40, 30, 20, 10

sol = odeint(dfdt, y0 = [S0, E0, I0, R0], t = times, args = (a, r, b, c))

# print(sol)

plt.figure(figsize = (4.5, 4))
plt.plot(times, sol.T[0], label = 'Susceptible', lw = 1.5)
plt.plot(times, sol.T[1], label = 'Exposed', lw = 1.5)
plt.plot(times, sol.T[2], label = 'Infected', lw = 1.5)
plt.plot(times, sol.T[3], label = 'Recovered', lw = 1.5)

plt.xlim(min(times), max(times))

plt.xlabel('Times [days]')
plt.ylabel('$S(t), E(t), I(t), R(t)$')

plt.legend(fontsize = 11)

plt.savefig(".\\plots_with_matplolib\\solve_de\\Ref_SEIR_plot.png", dpi = 200, bbox_inches = "tight")

# plt.show()