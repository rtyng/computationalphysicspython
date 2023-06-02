import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure and axis for animation
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# Set labels and title
# Fraction remaining refers to the portion of radioactive particles that have not decayed at a particular time
ax.set_xlabel("Time")
ax.set_ylabel("Fraction Remaining") 
ax.set_title("Radioactive Decay Simulation")

# Function to initialize the animation
def init():
    ax.set_xlim(0, 100)  # Set x-axis limits
    ax.set_ylim(0, 1)    # Set y-axis limits
    return line,

# Function to update the animation frame
def update(frame):
    # Generate random decay events
    decayed = np.random.random(100) < 0.01 * frame
    
    # Calculate the fraction of remaining particles
    fraction_remaining = np.sum(decayed) / 100
    
    # Update the plot data
    line.set_xdata(np.arange(frame+1))  # Update x-data
    line.set_ydata(np.full(frame+1, fraction_remaining))  # Update y-data
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(101), init_func=init, blit=True)

# Show the animation
plt.show()
