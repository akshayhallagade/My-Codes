import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 1000)
y = np.sin(x)
fig = plt.figure()
ax = plt.axes()
ax.plot(x, y)
plt.xlabel("x-axis")  # Adds label for the x-line.
plt.ylabel("y-axis")  # Adds label for the y-line.
plt.title("Function sin(x)")  # Creates title.
plt.xlim(0, 10)  # set limit for x-axis.
plt.ylim(-5, 5)  # set limit for y-axis.
plt.savefig("3. Data Visualization/fig2.png")
plt.show()
