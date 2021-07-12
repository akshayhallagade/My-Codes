import pandas as pd
presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')  # read
# shows type of series of "abraham lincoln".
print(type(presidents_df.loc["Abraham Lincoln"]))
# shows shape of series of "abraham lincoln".
print(presidents_df.loc["Abraham Lincoln"].shape)
# shows series from "Abraham Lincoln" to "Ulsses S. Grant".
print(presidents_df.loc["Abraham Lincoln":"Ulysses S. Grant"])
########################################################
# # shows series from index".
# print(presidents_df.iloc[15])
