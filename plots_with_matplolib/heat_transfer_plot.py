# import required libraries
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Use science style
plt.style.use(["science", "notebook", "grid"])

t = np.linspace(0, 70, 100)

T = 100-(4*t+20)*np.exp(-0.1*t)
Tm = 100-40*np.exp(-0.1*t)

plt.figure(figsize=(5, 4))
plt.plot(t, T, color = 'red', label = 'Heat transfer per $s$')
plt.plot(t, Tm, color = 'blue', label = 'Ambient heat transfer per $s$')

plt.xlabel("Time [s]", fontsize = 14)
plt.ylabel("Heat transfer $[C^0]$", fontsize = 14)
plt.xlim(min(t), max(t))

plt.tick_params(which = 'both', labelsize = 12)

plt.legend(fontsize = 10)

plt.grid(True)
plt.savefig(".\\plots_with_matplolib\\heat.png", dpi = 200, bbox_inches = "tight")
#plt.show()
