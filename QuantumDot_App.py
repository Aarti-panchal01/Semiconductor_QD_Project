import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App title
st.title("Quantum Dot Energy Level Simulator")

# App description
st.markdown("""
This app simulates the quantum confinement effect in quantum dots (QDs) using a particle-in-a-box model.
Explore how energy levels vary with dot size and quantum number.
""")

# Input parameters
L_min = st.slider("Minimum Quantum Dot Size (nm)", 1, 5, 1)
L_max = st.slider("Maximum Quantum Dot Size (nm)", 6, 20, 10)
n_max = st.slider("Maximum Quantum Number (n)", 1, 5, 3)

# Constants
h = 6.626e-34  # Planck's constant (J·s)
m = 9.11e-31   # Electron mass (kg)

# Quantum dot sizes
L_nm = np.linspace(L_min, L_max, 200)
L = L_nm * 1e-9  # Convert to meters

# Calculate and plot energy levels
fig, ax = plt.subplots(figsize=(10, 5))
for n in range(1, n_max + 1):
    E = (n**2 * h**2) / (8 * m * L**2) / 1.6e-19  # in eV
    ax.plot(L_nm, E, label=f'n = {n}')

ax.set_title("Energy Levels in Quantum Dots")
ax.set_xlabel("Quantum Dot Size (nm)")
ax.set_ylabel("Energy (eV)")
ax.legend()
ax.grid(True)

st.pyplot(fig)

st.markdown("""
**Interpretation**: As the size of the quantum dot decreases, energy levels increase and become more widely spaced.
This principle is key to semiconductor QD device design.
""")
