# import required libraries
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Use science style
plt.style.use(["science", "notebook", "grid"])


res1 = np.random.normal(loc=50, scale=10, size=1000)
res2 = np.random.normal(loc=50, scale=13, size=1000)

plt.figure(figsize=(8,3))
plt.hist(res1, bins = 30, histtype='step', density=True, label="res1")
plt.hist(res2, bins = 30, histtype='step', density=True, label="res2")

plt.legend()
plt.savefig(".\\plots_with_matplolib\\histogram.png", dpi = 200, bbox_inches = "tight")
#plt.show()
