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

# Create a plot
plt.figure(figsize=(7, 5))

for k in k_values:
    # Calculate T for each k
    T = 100 - (4 * t + 20) * np.exp(-0.1 * t * k)
    plt.plot(t, T, label=f'k = {k}')

# Add the ambient heat transfer line
Tm = 100 - 40 * np.exp(-0.1 * t)
#plt.plot(t, Tm, color='blue', linestyle='--', label='Ambient heat transfer per $s$')

# Labeling and grid
plt.xlabel("Time [s]", fontsize=14)
plt.ylabel("Heat transfer $[C^0]$", fontsize=14)
plt.xlim(min(t), max(t))
plt.tick_params(which='both', labelsize=12)
plt.legend(fontsize=9, loc='upper left', handlelength=3, fancybox= False, edgecolor= 'black', facecolor = 'white', labelspacing=0.1)
plt.grid(True)

plt.savefig(".\\plots_with_matplolib\\heat_multiple_lines.png", dpi = 200, bbox_inches = "tight")
# Show plot
plt.show()
