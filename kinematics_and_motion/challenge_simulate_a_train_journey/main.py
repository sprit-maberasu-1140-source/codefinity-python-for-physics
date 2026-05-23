def train_position(time, segments):
    # Write your code here
    
    position = 0
    elapsed= 0

    for segment in segments:
        duration = segment["duration"]
        velocity = segment["velocity"]
        if time < elapsed + duration:
            position += velocity * (time - elapsed)
            return position
        position += velocity * duration
        elapsed += duration
    return position

segments = [
    {"duration": 10, "velocity": 60},
    {"duration": 5, "velocity": 0},
    {"duration": 15, "velocity": 80}
]

pos1 = train_position(8, segments)
print(pos1)
pos2 = train_position(12, segments)
print(pos2)
pos3 = train_position(20, segments)
print(pos3)
pos4 = train_position(30, segments)
print(pos4)
