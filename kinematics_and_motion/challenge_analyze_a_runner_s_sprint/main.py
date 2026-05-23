import pandas as pd
import matplotlib.pyplot as plt

# Create a sample CSV file with sprint data
sample_data = {
    'time': [0, 1, 2, 3, 4, 5],
    'position': [0, 2, 6, 12, 20, 30]
}
df = pd.DataFrame(sample_data)
df.to_csv('sprint_data.csv', index=False)

def analyze_sprint(filename):
    data = pd.read_csv(filename)
    time = data['time']
    position = data['position']
    
    # Calculate instantaneous speed (first derivative)
    speed = position.diff() / time.diff()
    # Calculate average speed for the whole run
    total_distance = position.iloc[-1] - position.iloc[0]
    total_time = time.iloc[-1] - time.iloc[0]
    avg_speed_result = total_distance / total_time
    
    # Calculate instantaneous acceleration (second derivative)
    acceleration = speed.diff() / time.diff()
    # Calculate average acceleration for the whole run
    total_speed_change = speed.iloc[-1] - speed.iloc[1]
    avg_acceleration_result = total_speed_change / total_time
    
    # Plot position vs. time
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(time, position, marker='o')
    plt.title("Runner's Position Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Position (m)")
    
    # Plot speed vs. time
    plt.subplot(3, 1, 2)
    plt.plot(time, speed, marker='o', color='g')
    plt.title("Runner's Speed Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Speed (m/s)")
    
    # Plot acceleration vs. time
    plt.subplot(3, 1, 3)
    plt.plot(time, acceleration, marker='o', color='r')
    plt.title("Runner's Acceleration Over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (m/s²)")
    
    plt.tight_layout()
    plt.show()
    
    print("Average Speed:", avg_speed_result)
    print("Average Acceleration:", avg_acceleration_result)
    return avg_speed_result, avg_acceleration_result

# Sample call (creates and uses 'sprint_data.csv')
analyze_sprint('sprint_data.csv')