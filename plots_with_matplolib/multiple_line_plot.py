# import required libraries
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Use science style
plt.style.use(["science", "notebook", "grid"])

# Create domain-data and range-data
x1 = np.linspace(0, 15, 30)
x2 = np.linspace(0,15, 100)
y1 = np.sin(x1) + 0.1 * np.random.randn(len(x1))
y2 = np.sin(x2)

# Plot the data

plt.figure(figsize=(10,3))
plt.plot(x1, y1, linestyle = '', color = 'purple', linewidth = 1.5, 
         marker = 'o', markerfacecolor = 'blue', markeredgecolor = 'black',  markeredgewidth = 1.0, markersize = 6,
         label="$f_1$ sine wave")

plt.plot(x2, y2, linestyle = '-', color = 'red', linewidth = 1.5, 
#         marker = 'o', markerfacecolor = 'gold', markeredgecolor = 'black',  markeredgewidth = 1.5, markersize = 8,
         label="$f_2$ sine wave")
plt.xlabel("Time [s]") # x-axis label
plt.ylabel("Voltage [v]") # y-axis label
#plt.legend(loc = "lower right" , fontsize = 10)
plt.legend(loc = "lower right" , fontsize = 10, ncol = 2)

plt.xlim(min(x1), max(x1))


plt.savefig(".\\plots_with_matplolib\\multi_line.png", dpi = 200, bbox_inches = "tight")
#plt.show()
