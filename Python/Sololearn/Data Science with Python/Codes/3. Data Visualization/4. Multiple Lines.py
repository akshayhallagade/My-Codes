# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(0, 10, 1000)
# y = np.sin(x)
# fig = plt.figure()
# ax = plt.axes()
# ax.plot(x, np.sin(x))
# ax.plot(x, np.cos(x))
# writting multiplt graphs line in a graph.
# plt.savefig("3. Data Visualization/fig3.png")
# plt.show()
#####################################

import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 1000)
y = np.sin(x)
fig = plt.figure()
ax = plt.axes()
ax.plot(x, np.sin(x), color="k", linestyle=":", label="sin(x)")
ax.plot(x, np.cos(x), color="r", linestyle="--", label="cos(x)")
plt.legend()
# selecting a different color of the multiple graph lines.
"""
    k=black
    g=green
    r=red
    c=cyan
    y=yellow
    b=blue
    m=magenta
    w=white
    : = dotted Line      
    -- = Dashed line
"""
# selecting different styles for the graph lines.
plt.savefig("3. Data Visualization/fig3.png")
plt.show()
