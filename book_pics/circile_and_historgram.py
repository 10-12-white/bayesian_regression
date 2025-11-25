import matplotlib.pyplot as plt
import numpy as np

def plot_circle_rings():
    """Plots concentric circles."""
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_alpha(0)
    ax.add_patch(plt.Circle((0, 0), 1, fill=False, linewidth=2))
    ax.add_patch(plt.Circle((0, 0), 0.5, fill=False))
    ax.add_patch(plt.Circle((0, 0), 2, fill=False, linewidth=1))
    ax.add_patch(plt.Circle((0, 0), 1.5, fill=False, color='gray'))
    ax.add_patch(plt.Circle((0, 0), 0.5, fill=False, color='gray'))
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal')  # Ensure circles are circular
    ax.set_facecolor('none') #Transparent background
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

    ax.text(0, 2, '2', ha='center', va='bottom')
    ax.text(0, 1, '1', ha='center', va='bottom')
    ax.text(0, 1.5, '1.5', ha='center', va='bottom')
    ax.text(0, 0.5, '0.5', ha='center', va='bottom')

    return fig, ax

def plot_histogram():
    """Plots the histogram of probabilities."""
    r_values = [0.5, 1, 1.5, 2]
    probabilities = [1/16, 3/16, 5/16, 7/16]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(r_values, probabilities, width=0.3)
    fig.patch.set_alpha(0)
    ax.set_xlabel('$r$')
    ax.set_ylabel('Probability')
    ax.set_title('Histogram of Probabilities at Values of $r$')
    ax.set_xlim(0.05, 2.125)
    ax.set_ylim(0, 0.5)
    ax.set_xticks(r_values)

    for x, y in zip(r_values, probabilities):
        ax.text(x, y, f'{y:.3f}', ha='center', va='bottom')

    ax.set_facecolor('none') #Transparent background
    #fig.savefig("Histogram.pdf", dpi="300")
    return fig, ax
    


import matplotlib.pyplot as plt
import numpy as np

def plot_gaussian_distributions():
    """Plots two Gaussian distributions with different standard deviations and adds annotations."""
    x = np.linspace(-4, 4, 1000)
    y1 = np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)
    y2 = np.exp(-x**2 / (2 * 0.5**2)) / (0.5 * np.sqrt(2 * np.pi))

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y1, label='Lower confidence results in larger range of errors. SD = 1', linewidth = 3, color='blue')
    ax.plot(x, y2, label='Higher confidence results in smaller range of errors. SD = 0.5', linewidth = 3, color='red')
    ax.axvline(0, color='gray', linestyle='--')  # Median line
    ax.set_title('Same mean, different standard deviations (SD)')
    ax.set_xlabel('The size our error')
    ax.set_ylabel('Likelihood of our error')
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 1)
    ax.set_xticks([])  # Remove x-ticks
    ax.legend()
    fig.patch.set_alpha(0) # Transparent background
    ax.set_facecolor('none')
    plt.show()
    
# Generate and display the plots
fig_circle, ax_circle = plot_circle_rings()
fig_hist, ax_hist = plot_histogram()
plt.show() # Display both plots
plot_gaussian_distributions()
