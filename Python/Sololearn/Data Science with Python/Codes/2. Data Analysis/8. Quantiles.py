""".....................Quantiles....................
This are the cut points dividing the range of the data into 
continuous intervals with an equal number of observations.
"""

import pandas as pd
presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
print(presidents_df['age'].quantile([0.25, 0.5, 0.75, 1]))
