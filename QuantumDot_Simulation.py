"""
Quantum Dot Simulation in a Semiconductor Matrix

This script simulates quantum confinement effects in quantum dots (QDs) using
a 1D particle-in-a-box model and visualizes energy level changes with QD size.
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34  # Planck's constant (J·s)
m = 9.11e-31   # Electron mass (kg)

# Quantum dot size (L in nm)
L_nm = np.linspace(1, 10, 100)
L = L_nm * 1e-9  # Convert to meters

# Calculate energy levels for n = 1, 2, 3
n_values = [1, 2, 3]
energies = {n: (n**2 * h**2) / (8 * m * L**2) / 1.6e-19 for n in n_values}  # in eV

# Plot
plt.figure(figsize=(10, 6))
for n, E in energies.items():
    plt.plot(L_nm, E, label=f'n = {n}')

plt.title('Energy Levels in a Quantum Dot vs. Dot Size')
plt.xlabel('Quantum Dot Size (nm)')
plt.ylabel('Energy Level (eV)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
