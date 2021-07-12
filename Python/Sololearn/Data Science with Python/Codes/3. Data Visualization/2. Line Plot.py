import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 1000)  # x is a 1000 evenly spaced numbers from 0 to 10.
y = np.sin(x)  # tides are created using the sin function.
fig = plt.figure()  # to show plot.
ax = plt.axes()  # to show axes.
ax.plot(x, y)  # plot the graph.
plt.savefig("3. Data Visualization/fig1.png")
# save the graph image which is created.
plt.show()  # show graph.
