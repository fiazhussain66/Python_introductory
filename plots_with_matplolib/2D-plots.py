import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'notebook', 'grid'])

x= np.linspace(-5,5,100)
y = np.linspace(-5,5,100)

X, Y = np.meshgrid(x, y)

x0 = -2
x1 = +2
def f(x, y):
    return (x-x0)/np.sqrt((x-x0)**2+y**2) - (x-x1)/np.sqrt((x-x1)**2+y**2)


z = f(X, Y)
E = -abs(1/np.sqrt((X-x0)**2+Y**2) - 1/np.sqrt((X-x1)**2+Y**2))

fig, ax = plt.subplots(figsize=(5, 4))


c0 = plt.contour(X, Y, z, levels = 10, colors = 'black', linestyles = '-', linewidths = 0.8, zorder = 1)
plt.contour(X, Y, E, levels = [-0.5, -0.4, -0.3, -0.2, -0.1, -0.05], colors = 'black', linestyles = '-.', linewidths = 0.8, zorder = 1)
c1 = plt.contourf(X, Y, z, levels = 10, cmap = 'rainbow', zorder = 0)

cbar = plt.colorbar(c1, pad = 0.05)
cbar.ax.minorticks_on()
cbar.ax.tick_params(axis='y', which='major', length=7, width=1.5, direction='in', labelsize=12, zorder=3)
cbar.ax.tick_params(axis='y', which='minor', length=4, width=1.2, direction='in', zorder=3)

# Adjusting tick z-order manually (this should force the ticks to render above contours)
for tick in cbar.ax.get_yticklabels(minor=False):
    tick.set_zorder(4)
for tick in cbar.ax.get_yticklabels(minor=True):
    tick.set_zorder(4)

plt.xlabel('x-axes')
plt.ylabel('y-axes')

plt.minorticks_on()
plt.tick_params(direction='in', which='minor', length=3, bottom=True, top=True, left=True, right=True, zorder = 2)
plt.tick_params(direction='in', which='major', length=7, bottom=True, top=True, left=True, right=True, zorder = 2)
plt.tick_params(which = 'both', direction = 'in', labelsize = 12)


plt.savefig('.\\plots_with_matplolib\\2D-plot.png', dpi=250, bbox_inches = 'tight')
#plt.show()