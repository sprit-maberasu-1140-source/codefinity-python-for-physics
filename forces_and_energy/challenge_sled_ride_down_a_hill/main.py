import numpy as np
import matplotlib.pyplot as plt

def simulate_sled(mass, slope_angle_deg, mu, hill_length):
    g = 9.81
    theta = np.deg2rad(slope_angle_deg)
    a = g * (np.sin(theta) - mu * np.cos(theta))
    if a <= 0:
        final_speed = 0.0
        distance = 0.0
    else:
        final_speed = np.sqrt(2 * a * hill_length)
        distance = hill_length
    return final_speed, distance

def plot_sled_results(mass, hill_length, mu_values, slope_angles):
    for mu in mu_values:
        speeds = []
        for angle in slope_angles:
            speed, _ = simulate_sled(mass, angle, mu, hill_length)
            speeds.append(speed)
        plt.plot(slope_angles, speeds, label=f"μ={mu}")
    plt.xlabel("Slope Angle (degrees)")
    plt.ylabel("Final Speed (m/s)")
    plt.title("Sled Final Speed vs. Slope Angle for Different Friction Coefficients")
    plt.legend()
    plt.grid(True)
    plt.show()

mass = 50  # kg
hill_length = 100  # meters
mu_values = [0.05, 0.15, 0.3]
slope_angles = np.linspace(5, 45, 9)

plot_sled_results(mass, hill_length, mu_values, slope_angles)

final_speed, distance = simulate_sled(mass, 20, 0.1, hill_length)
result_speed = final_speed
result_distance = distance
print("Final speed:", result_speed)
print("Distance traveled:", result_distance)