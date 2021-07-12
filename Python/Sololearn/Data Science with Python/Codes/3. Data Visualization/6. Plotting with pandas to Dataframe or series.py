import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
presidents_df.plot(kind="scatter", x="height",
                   y="age", title="U.S. Presidents")
plt.savefig("3. Data visualization/fig5.png")
plt.show()
