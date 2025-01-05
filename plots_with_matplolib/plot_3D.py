import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import projections
import scienceplots

plt.style.use(['science', 'notebook', 'grid'])

def f(x, y):
    return x**2 + y**2

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(111, projection='3d', aspect='auto')
surf = ax.plot_surface(X, Y, Z, cmap='rainbow', edgecolor = 'black', linewidth = 0.5)  
cbar = plt.colorbar(surf, shrink=0.5, aspect=10, pad = 0.08)
cbar.ax.tick_params(labelsize=10)
cbar.ax.yaxis.set_ticks_position('right')

ax.view_init(elev=30, azim=-45)

ax.set_xlabel("x-axes", fontsize = 12)
ax.set_ylabel("y-axes", fontsize = 12)
ax.set_zlabel("f(x,y)", fontsize = 12)

ax.set_box_aspect([1, 0.92, 0.82])

ax.tick_params(which = 'both', labelsize = 11)

ax.grid(True, color = 'grey', alpha = 0.2)

plt.title("3D plot of the function.")
plt.savefig('.\\plots_with_matplolib\\3D-plot.png', dpi=250, bbox_inches = 'tight')

plt.show()
