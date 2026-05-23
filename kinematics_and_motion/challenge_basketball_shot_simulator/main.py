import math

def basketball_shot_scores(initial_speed, launch_angle_deg, hoop_x, hoop_y, hoop_radius=0.23):
    # Write your code here

    if not isinstance(initial_speed,(int,float)):
        return False
    if initial_speed <= 0:
        return False

    angle = float(launch_angle_deg)
    if angle <= 0 or angle >= 90:
        return False

    g = 9.81
    theta = math.radians(angle)

    shot_range = (initial_speed ** 2) * math.sin(2 * theta) / g

    tolerance = 2.0 * float(hoop_radius)

    return shot_range + tolerance >= float(hoop_x)

# Sample calls
result1 = basketball_shot_scores(8.0, 50, 6.75, 3.05)
print(result1)
result2 = basketball_shot_scores(6.0, 40, 6.75, 3.05)
print(result2)
result3 = basketball_shot_scores(9.0, 60, 6.75, 3.05)
print(result3)
