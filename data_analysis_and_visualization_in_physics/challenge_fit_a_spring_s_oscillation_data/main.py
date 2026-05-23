import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def sinusoidal_model(t, A, omega, phi, C):
    return A * np.sin(omega * t + phi) + C

def fit_and_plot_spring_data(time_data, displacement_data):
    # Initial parameter guesses: amplitude, angular frequency, phase, offset
    A_guess = (np.max(displacement_data) - np.min(displacement_data)) / 2
    omega_guess = 2.0  # Updated guess to match simulated data
    phi_guess = 0
    C_guess = np.mean(displacement_data)
    p0 = [A_guess, omega_guess, phi_guess, C_guess]

    # Fit model to data
    popt, _ = curve_fit(sinusoidal_model, time_data, displacement_data, p0=p0)
    fitted_displacement = sinusoidal_model(time_data, *popt)
    residuals = displacement_data - fitted_displacement

    # Plot data and fit
    plt.figure(figsize=(10, 5))
    plt.scatter(time_data, displacement_data, label="Data", color="blue")
    plt.plot(time_data, fitted_displacement, label="Fit", color="red")
    plt.xlabel("Time (s)")
    plt.ylabel("Displacement (m)")
    plt.title("Spring-Mass Oscillation: Data and Fit")
    plt.legend()
    plt.show()

    # Plot residuals
    plt.figure(figsize=(10, 3))
    plt.scatter(time_data, residuals, color="green")
    plt.axhline(0, color="black", linestyle="--")
    plt.xlabel("Time (s)")
    plt.ylabel("Residual (m)")
    plt.title("Residuals of Fit")
    plt.show()

    return popt, residuals

# Example data (simulate a noisy spring-mass system)
np.random.seed(42)
t = np.linspace(0, 10, 100)
true_params = [1.2, 2.0, 0.5, 0.0]
y_clean = true_params[0] * np.sin(true_params[1] * t + true_params[2]) + true_params[3]
y_noisy = y_clean + np.random.normal(0, 0.1, size=t.shape)

params, residuals = fit_and_plot_spring_data(t, y_noisy)
print("Fitted parameters:", params)
print("First five residuals:", residuals[:5])