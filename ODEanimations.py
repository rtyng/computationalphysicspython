"""
In order to strengthen the programming skills and to gain an appreciation 
of physics in python for use later in the c++ 2d and 3d engines
"""
import numpy as np
import matplotlib.pyplot as plt

class SimpleHarmonicOscillator:
    def __init__(self, mass, spring_constant, initial_displacement=0.0, initial_velocity=0.0):
        self.mass = mass
        self.spring_constant = spring_constant
        self.displacement = initial_displacement
        self.velocity = initial_velocity
        
    def update(self, time_step):
        acceleration = -self.spring_constant / self.mass * self.displacement
        self.velocity += acceleration * time_step
        self.displacement += self.velocity * time_step

    def get_displacement(self):
        return self.displacement
    

oscillator1 = SimpleHarmonicOscillator(mass=1.0, spring_constant=2.0)
oscillator2 = SimpleHarmonicOscillator(mass=0.5, spring_constant=1.0, initial_displacement=1.0)

time_step = 0.1
num_iterations = 100

displacements = []
for _ in range(num_iterations):
    oscillator1.update(time_step)
    oscillator2.update(time_step)
    displacements.append((oscillator1.get_displacement(), oscillator2.get_displacement()))
    

time = np.arange(0, num_iterations * time_step, time_step)
displacements = np.array(displacements)

plt.plot(time, displacements[:, 0], label='Oscillator 1')
plt.plot(time, displacements[:, 1], label='Oscillator 2')
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.legend()
plt.grid(True)
plt.show()