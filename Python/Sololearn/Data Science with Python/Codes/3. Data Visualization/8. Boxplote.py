import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
presidents_df.boxplot(column='height')
plt.savefig("3. Data visualization/fig7.png")
plt.show()
