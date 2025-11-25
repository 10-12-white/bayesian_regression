import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter

# Sample data points (estimated from the image)
x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([1, 4, 3, 3.5, 5, 4, 4.5])  # Approximate y-values

# 1. Plotting the Data Points
plt.figure(figsize=(8, 6), facecolor='none')  # Transparent background
plt.scatter(x, y, color='red', s=50)

# 2. Interpolated Line (using cubic interpolation)
f_interp = interp1d(x, y, kind='cubic')
x_interp = np.linspace(min(x), max(x), 500)  # More points for a smoother curve
y_interp = f_interp(x_interp)
plt.plot(x_interp, y_interp, color='blue', linewidth=2)

# 3. Smoothed Line (using Savitzky-Golay filter)
y_smooth = savgol_filter(y, window_length=5, polyorder=2)  # Adjust window_length and polyorder as needed
x_smooth = np.linspace(min(x), max(x), 500)
f_smooth = interp1d(x, y_smooth, kind='cubic')  # Interpolate the smoothed points
y_smooth_interp = f_smooth(x_smooth)
plt.plot(x_smooth, y_smooth_interp, color='green', linewidth=2)

# 4. Setting Plot Properties
plt.xlabel('X', fontsize=14)
plt.ylabel('y', fontsize=14, rotation=0)  # Keep y-label horizontal
plt.xticks([])  # Remove x-ticks
plt.yticks([])  # Remove y-ticks
plt.box(False)  # Remove the outer box

# 5. Saving the Image
plt.savefig('replicated_graph.png', transparent=True)
plt.show()