import numpy as np
import matplotlib.pyplot as plt

# Set up the parameters
mass = 1.0       # Mass of the oscillator
k = 1.0          # Spring constant
omega = np.sqrt(k/mass)   # Angular frequency

# Set up the time range
t = np.linspace(0, 10, 1000)   # Time values from 0 to 10 seconds

# Compute the displacement of the oscillator in x and y directions as a function of time
x = np.cos(omega * t)
y = np.sin(omega * t)

# Plot the motion of the oscillator in 2D
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple Harmonic Oscillator - Motion in 2D')
plt.grid(True)
plt.axis('equal')   # Set equal scaling for x and y axes
plt.show()