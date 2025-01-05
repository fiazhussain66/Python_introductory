from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(['science', 'notebook', 'grid'])

def dAdt(A, t, beta, gamma, N):
    S = A[0]
    I = A[1]
    R = A[2]
    return [
        -beta/N * S * I,
        beta/N * S * I - gamma * I,
        gamma * I
    ]

times = np.linspace(0, 100, 100)

gamma = 1/10
N = 1.1e7
S0, I0, R0 = N - 574, 574, 0

# Define the range of beta values to iterate over
vary_values = [0.33, 0.35, 0.37, 0.39]

# Create a figure with 3 subplots (one for each population)
fig, axs = plt.subplots(3, 1, figsize=(8, 6.5))
plt.subplots_adjust(wspace=0.0, hspace=0.1)

# Plot each population (S, I, R) in a separate subplot
for beta in vary_values:
    sol = odeint(dAdt, y0=[S0, I0, R0], t=times, args=(beta, gamma, N))
    S = sol.T[0]
    I = sol.T[1]
    R = sol.T[2]

    # Plot Susceptible (S)
    axs[0].plot(times, S, label=f"$\\beta={beta}$")

    # Plot Infected (I)
    axs[1].plot(times, I, label=f"$\\beta={beta}$")

    # Plot Recovered (R)
    axs[2].plot(times, R, label=f"$\\beta={beta}$")



axs[0].tick_params(which = 'both', labelbottom=False, labelsize = 11)
axs[1].tick_params(which = 'both', labelbottom=False, labelsize = 11)
axs[2].tick_params(which = 'both', labelbottom=True, labelsize = 11)

axs[0].set_ylabel("Population")
axs[0].legend(fontsize = 7)

#axs[1].set_title("Infected Population (I)")
axs[1].set_ylabel("Population")
axs[1].legend(fontsize = 7)

#axs[2].set_title("Recovered Population (R)")
axs[2].set_xlabel("Time (days)")
axs[2].set_ylabel("Population")
axs[2].legend(loc = 'lower right', fontsize = 7)

plt.savefig(".\\solve_de\\multi_SEIR_plot.png", dpi = 200, bbox_inches = "tight")


# plt.show()