import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
party_cnt = presidents_df["party"].value_counts()

plt.style.use('ggplot')
party_cnt.plot(kind="bar")
plt.savefig("3. Data visualization/fig8.png")
plt.show()
