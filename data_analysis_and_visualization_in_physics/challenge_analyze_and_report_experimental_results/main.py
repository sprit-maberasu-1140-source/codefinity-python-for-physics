import numpy as np
import matplotlib.pyplot as plt

def analyze_experiment(data, uncertainties):
    # Compute mean and standard deviation for the main measurement
    mean_value = np.mean(data)
    std_dev = np.std(data, ddof=1)
    
    # Propagate uncertainty: combine standard deviation and given uncertainties
    mean_uncertainty = np.mean(uncertainties)
    total_uncertainty = np.sqrt(std_dev**2 + mean_uncertainty**2)
    
    # Create summary string
    summary = f"Mean value: {mean_value:.2f}\n"
    summary += f"Standard deviation: {std_dev:.2f}\n"
    summary += f"Propagated uncertainty: {total_uncertainty:.2f}"
    
    # Plot data with error bars
    x_values = np.arange(1, len(data) + 1)
    plt.errorbar(x_values, data, yerr=uncertainties, fmt='o', label='Measurements')
    plt.axhline(mean_value, color='red', linestyle='--', label='Mean')
    plt.xlabel('Trial')
    plt.ylabel('Measured Value')
    plt.title('Experimental Data with Uncertainties')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    print(summary)
    return mean_value, std_dev, total_uncertainty

data = [9.81, 9.78, 9.85, 9.80, 9.83]
uncertainties = [0.02, 0.02, 0.03, 0.02, 0.02]

mean_value, std_dev, total_uncertainty = analyze_experiment(data, uncertainties)