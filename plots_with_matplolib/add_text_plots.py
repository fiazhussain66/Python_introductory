# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Use science style
plt.style.use(["science", "notebook", "grid"])

# Define time array
t = np.linspace(0, 70, 100)

# Define multiple values of k
k_values = [1.0, 1.1, 1.2, 1.3, 1.4]


fig, axes = plt.subplots(1,2, figsize = (10, 4))

ax = axes[0]

for k in k_values:
    # Calculate T for each k
    T = 100 - (4 * t + 20) * np.exp(-0.1 * t * k)
    ax.plot(t, T, label=f'k = {k}', linewidth = 1.5)

# Labeling and grid
ax.set_xlabel("Time [s]", fontsize=14)
ax.set_ylabel("Heat transfer $[C^0]$", fontsize=14)
ax.set_xlim(min(t), max(t))
ax.tick_params(which='both', labelsize=12)

ax.text(0.5, 0.13, 
        r"$Nt=0.2$, $Nb=0.2$, $Br=2.5$" "\n"
        r"$Gr=0.5$, $\beta=1.8$, $\delta_1=0.2$", 
        transform=ax.transAxes,
        bbox=dict(facecolor = 'white', edgecolor= 'black'),
        fontsize=9, ha='center')


ax.legend(fontsize=9, loc='upper left', handlelength=1.5, fancybox= False, edgecolor= 'black', facecolor = 'white', labelspacing=0.1)
ax.grid(True)

ax = axes[1]

for k in k_values:
    # Calculate T for each k
    Tm = 100 - 40 * np.exp(-0.1 * t*k)
    ax.plot(t, Tm, label=f'k = {k}', linewidth = 1.5)

# Labeling and grid
ax.set_xlabel("Time [s]", fontsize=14)
ax.set_ylabel("Heat transfer $[C^0]$", fontsize=14)
ax.set_xlim(min(t), max(t))
ax.tick_params(which='both', labelsize=12)

ax.text(0.5, 0.13, 
        r"$Nt=0.2$, $Nb=0.2$, $Br=2.5$" "\n"
        r"$Gr=0.5$, $\beta=1.8$, $\delta_1=0.2$", 
        transform=ax.transAxes,
        bbox=dict(facecolor = 'white', edgecolor= 'black'),
        fontsize=9, ha='center')


ax.legend(fontsize=9, loc='upper left', handlelength=1.5, fancybox= False, edgecolor= 'black', facecolor = 'white', labelspacing=0.1)
ax.grid(True)

plt.savefig(".\\plots_with_matplolib\\add_text_plots.png", dpi = 200, bbox_inches = "tight")


plt.show()