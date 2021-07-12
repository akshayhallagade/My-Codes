# import pandas as pd
# presidents_df = pd.read_csv(
#     'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# print(presidents_df.groupby("party").mean())
################################################
import pandas as pd
import numpy as np
presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
print(presidents_df.groupby('party')["height"].agg(["min", np.median, max]))
################################################
