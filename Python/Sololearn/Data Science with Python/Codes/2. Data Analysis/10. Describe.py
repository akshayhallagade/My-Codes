# import pandas as pd
# presidents_df = pd.read_csv(
#     'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# # gives count, mean, std, min, 25%, 50%, 75%, max.
# print(presidents_df["age"].describe())  # gives inforamtion about column.
# print(presidents_df.describe())  # gives information about dataframe.
################################################
# value_count
import pandas as pd
presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# gives count, mean, std, min, 25%, 50%, 75%, max.
print(presidents_df["party"].value_counts())
