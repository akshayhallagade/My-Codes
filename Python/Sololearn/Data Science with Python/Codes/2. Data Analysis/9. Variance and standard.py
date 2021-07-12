# import pandas as pd
# const = pd.Series([2, 2, 2])
# writes variance.
# print(const.var())
# writes Standard Deviation.
# print(const.std())
######################
# import pandas as pd
# const = pd.Series([2, 3, 4])
# print(const.var())
# print(const.std())
######################
# import pandas as pd
# presidents_df = pd.read_csv(
#     'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# print(presidents_df['age'].var())
# print(presidents_df['age'].std())
# # gives variance and standard Deviation of given column.
######################
import pandas as pd
presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
print(presidents_df.std())
# gives column wise variance and standard Deviation.
