import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def analyze_pendulum(time, angle):
    # Plot angle vs. time
    plt.figure(figsize=(8, 4))
    plt.plot(time, angle, label="Pendulum Angle")
    plt.xlabel("Time (s)")
    plt.ylabel("Angle (degrees)")
    plt.title("Pendulum Oscillation")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Find peaks to estimate period
    peaks, _ = find_peaks(angle)
    peak_times = time[peaks]
    if len(peak_times) > 1:
        periods = np.diff(peak_times)
        computed_period = np.mean(periods)
    else:
        computed_period = None

    print(computed_period)
    return computed_period

# Sample data for demonstration
time = np.linspace(0, 10, 500)
angle = 20 * np.cos(2 * np.pi * time / 2.5)  # period ~2.5s

computed_period = analyze_pendulum(time, angle)