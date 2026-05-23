import numpy as np
import matplotlib.pyplot as plt

def roller_coaster_energy_analysis(mass, heights, velocities, g=9.81):
    # Calculate potential energy at each position using PE = mass * g * height
    potential_energy = mass * g * heights
    # Calculate kinetic energy at each position using KE = 0.5 * mass * velocity^2
    kinetic_energy = 0.5 * mass * velocities ** 2
    # Calculate total mechanical energy by summing PE and KE
    total_energy = potential_energy + kinetic_energy

    # Generate positions along the track for plotting (as array indices)
    positions = np.arange(len(heights))

    # Plot all three energy types
    plt.plot(positions, potential_energy, label="Potential Energy")
    plt.plot(positions, kinetic_energy, label="Kinetic Energy")
    plt.plot(positions, total_energy, label="Total Energy", linestyle="--")
    plt.xlabel("Track Position")
    plt.ylabel("Energy (Joules)")
    plt.title("Roller Coaster Energy Analysis")
    plt.legend()
    plt.show()

    # Return the calculated arrays
    return potential_energy, kinetic_energy, total_energy

# Sample data for demonstration
mass = 500  # kg
heights = np.array([30, 25, 20, 15, 10, 5, 0, 5, 10, 15])  # meters
velocities = np.array([0, 5, 10, 15, 20, 22, 24, 20, 15, 10])  # m/s

potential_energy, kinetic_energy, total_energy = roller_coaster_energy_analysis(mass, heights, velocities)