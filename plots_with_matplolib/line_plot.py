# import required libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Use science style
plt.style.use(["science", "notebook", "grid"])

# Create domain-data and range-data
x = np.linspace(0, 15, 30)
np.random.seed(42)  # For reproducibility
y = np.sin(x) + 0.1 * np.random.randn(len(x))

# Plot the data

plt.figure(figsize=(8,3.5))
plt.plot(x, y, linestyle = '--', color = 'purple', linewidth = 1.5, 
         marker = 'o', markerfacecolor = 'gold', markeredgecolor = 'black',  markeredgewidth = 1.5, markersize = 8,
         label="Sine Wave")
plt.xlabel("Time [s]") # x-axis label
plt.ylabel("Voltage [v]") # y-axis label

plt.legend(loc = "upper right", fontsize = 10)

plt.xlim(min(x), max(x))


plt.savefig(".\\plots_with_matplolib\\line.png", dpi = 200, bbox_inches = "tight")
#plt.show()
