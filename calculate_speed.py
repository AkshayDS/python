# Problem: Calculate Speed
# Description: Write a function `calculate_speed(distance, time)` that returns the speed.
# Formula: Speed = Distance / Time

def calculate_speed(distance, time):
    if time == 0:
        return "Time cannot be zero"
    return distance / time

# Basic Example
if __name__ == "__main__":
    d = 150  # distance in km
    t = 2.5  # time in hours
    speed = calculate_speed(d, t)
    print(f"For a distance of {d}km and time of {t} hours, the speed is: {speed} km/h")

    # Another example
    d2 = 300
    t2 = 5
    print(f"Distance: {d2}km, Time: {t2}h -> Speed: {calculate_speed(d2, t2)} km/h")
