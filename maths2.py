#Teht 1
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches

# Create figure and axis
fig, ax = plt.subplots()

# Create a unit circle at the origin
circle = patches.Circle((0, 0), radius=1, fill=False)
ax.add_patch(circle)

# Move left y-axis and bottom x-axis to center
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Hide top and right spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks only on the bottom and left axes
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# Set equal scaling
ax.axis('equal')

# Set custom ticks for x and y axes
plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])

# Define angles in degrees and corresponding colors
angles_deg = np.array([30, 45, 60, 90, 120, 150, 180, 270])
colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta', 'yellow']

# Convert angles to radians
angles_rad = np.radians(angles_deg)

# Compute x and y coordinates of points on the circle
x = np.cos(angles_rad)
y = np.sin(angles_rad)

# Scatter points on the circle
plt.scatter(x, y, color=colors, marker='X')

# Annotate each point with its angle in degrees
for i in range(len(angles_deg)):
    plt.annotate(f'{angles_deg[i]}°',
                 xy=(x[i], y[i]), xycoords='data',
                 xytext=(+10, +10), textcoords='offset points', fontsize=12,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

# Display plot
plt.show()

#Teht 2
import numpy as np
import matplotlib.pyplot as plt

# Määritellään x-arvot välillä -3π - 3π
x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)

# Määritellään käyrät: sin(x) ja cos(x)
y1 = np.sin(x)
y2 = np.cos(x)

# Muutetaan kuvaajan kokoa ja leveys kolminkertaiseksi
plt.figure(figsize=(19.2, 4.8))

# Piirretään käyrät, muutetaan värit ja piirto tyyli
plt.plot(x, y1, color='blue', linestyle='--', label='sin(x)')
plt.plot(x, y2, color='red', linestyle='-.', label='cos(x)')

# Lisätään selite
plt.legend()

# Näytetään kuvaaja
plt.show()

#Teht 3
import numpy as np
import matplotlib.pyplot as plt

# Määritellään x-arvot välillä -3π - 3π
x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)

# Määritellään käyrät: sin(x) ja cos(x)
y1 = np.sin(x)
y2 = np.cos(x)

# Muutetaan kuvaajan kokoa ja leveys kolminkertaiseksi
plt.figure(figsize=(19.2, 4.8))

# Piirretään käyrät, muutetaan värit ja piirto tyyli
plt.plot(x, y1, color='blue', linestyle='--', label='sin(x)')
plt.plot(x, y2, color='red', linestyle='-.', label='cos(x)')

# Asetetaan x-akselin tikit muotoon π, π/2 jne.
x_ticks = [-3*np.pi, -2.5*np.pi, -2*np.pi, -1.5*np.pi, -np.pi, -0.5*np.pi, 0, 0.5*np.pi, np.pi, 1.5*np.pi, 2*np.pi, 2.5*np.pi, 3*np.pi]
x_labels = [r'$-3\pi$', r'$-2.5\pi$', r'$-2\pi$', r'$-1.5\pi$', r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$', r'$\frac{5\pi}{2}$', r'$3\pi$']
plt.xticks(x_ticks, x_labels)

# Asetetaan y-akselin tikit (-1, 0, 1)
y_ticks = [-1, 0, 1]
y_labels = [r'$-1$', r'$0$', r'$1$']
plt.yticks(y_ticks, y_labels)

# Lisätään selite
plt.legend()

# Näytetään kuvaaja
plt.show()
