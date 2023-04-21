import numpy as np
import matplotlib.pyplot as plt
import mplcyberpunk

# Generate x values
x = np.linspace(0, 50, 50)

# Generate y values
y = np.sin(1/5*x)
y2 = np.cos(1/5*x)

plt.style.use('cyberpunk') # Set the style to cyberpunk
plt.figure(figsize = (6,4))


plt.scatter(x, y, marker = 'o')
plt.scatter(x, y2, marker = 'o', c='lime')
# mplcyberpunk.make_scatter_glow() # Make scatter glow

plt.plot(x, y, marker = 'o')
plt.plot(x, y2, marker = 'o', c='lime')

mplcyberpunk.make_lines_glow() # Make lines glow
mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.5, gradient_start='zero') # Add gradient fill

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.legend()

plt.show()