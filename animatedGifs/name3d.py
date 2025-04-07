import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Set up the figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Coordinates to place each letter
x = np.linspace(0, 10, 6)  # 6 letters in "Osanda"
y = np.sin(x)              # Add a wave-like pattern
z = np.cos(x)              # Adds 3D depth

# The letters of the name
name = "Osanda"

# Plot each letter in 3D space
for i, letter in enumerate(name):
    ax.text(x[i], y[i], z[i], letter, fontsize=20, color='purple')

# Set the viewing angle and axes
ax.set_title("3D Name: Osanda")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.view_init(elev=30, azim=45)

plt.show()
