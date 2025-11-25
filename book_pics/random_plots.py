import random
import matplotlib.pyplot as plt
import numpy as np

def generate_random_points(num_points=20, x_min=-2, x_max=2):
    """Generates a list of random points within the specified x range."""

    points = []
    for _ in range(num_points):
        x = random.uniform(x_min, x_max)
        y = random.uniform(0, 10)  # You can adjust the y range as needed
        points.append((x, y))
    return points

# Generate the points
points = generate_random_points()

# Separate x and y coordinates
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

# Create figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background color to black

# Plot the points
ax.scatter(x_coords, y_coords, color='yellow', marker='o')

# Add labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Random Points")
# Set x-axis limits
ax.set_xlim(-2, 2)

# Save and show the plot
plt.savefig("random_points_black_bg.png", facecolor='black') #saves the figure with a black background.
plt.show()


def generate_cubic_points(num_points=50, noise_factor=0.55):
    """Generates a list of points that closely fit y = x^3 with added noise."""

    points = []
    for _ in range(num_points):
        x = random.uniform(-5, 5)
        y = x**3 + random.uniform(-noise_factor * abs(x**3), noise_factor * abs(x**3))
        points.append((x, y))
    return points

# Generate the points
points = generate_cubic_points()

# Sort the points by x-value
points.sort(key=lambda point: point[0])

# Separate x and y coordinates
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

# Create figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background color to black

# Plot the points
ax.scatter(x_coords, y_coords, color='yellow', marker='o')

# Plot the line through the sorted points
ax.plot(x_coords, y_coords, color='red', linestyle='-', label="Line Through Points")

# Add labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Line Through Noisy Cubic Data (Bad Model)")
ax.grid(True, color='white')  # Set grid color to white

# Add legend
ax.legend()

# Save and show the plot
plt.savefig("bad_cubic_model_sorted.png", facecolor='black')
plt.show()

def generate_cubic_points(num_points=50, noise_factor=0.55):
    """Generates a list of points that closely fit y = x^3 with added noise."""

    points = []
    for _ in range(num_points):
        x = random.uniform(-5, 5)
        y = x**3 + random.uniform(-noise_factor * abs(x**3), noise_factor * abs(x**3))
        points.append((x, y))
    return points

# Generate the points
points = generate_cubic_points()

# Sort the points by x-value
points.sort(key=lambda point: point[0])

# Separate x and y coordinates
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

# Create figure and axes
fig, ax = plt.subplots()
ax.set_facecolor('black')  # Set background color to black

# Plot the points
ax.scatter(x_coords, y_coords, color='yellow', marker='o', label="Noisy Data Points")

# Plot the line through the sorted points (bad model)
ax.plot(x_coords, y_coords, color='red', linestyle='-', label="Line Through Points (Bad Model)")

# Plot the y = x^3 curve (good model)
x_curve = np.linspace(-5, 5, 100)  # Generate x values for the curve
y_curve = x_curve**3  # Calculate y values for the curve
ax.plot(x_curve, y_curve, color='green', linestyle='--', label="y = x^3 (Good Model)")

# Add labels and title
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Cubic Data and Models")
ax.grid(True, color='white')  # Set grid color to white

# Add legend
ax.legend()

# Save and show the plot
plt.savefig("cubic_models.png", facecolor='black')
plt.show()