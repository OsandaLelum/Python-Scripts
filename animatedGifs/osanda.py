import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.animation import FuncAnimation

# Setup the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Name and positions
name = "Osanda"
x = np.linspace(0, 10, len(name))
y = np.sin(x)
z = np.cos(x)

# Initial text objects (empty for now)
texts = [ax.text(x[i], y[i], z[i], name[i], fontsize=20, color='blue') for i in range(len(name))]

# Axis labels
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)
ax.set_title("Animated 3D Name: Osanda")

# Animation function
def update(frame):
    ax.view_init(elev=30, azim=frame)
    return texts

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 180, 2), interval=50, blit=False)

plt.show()
