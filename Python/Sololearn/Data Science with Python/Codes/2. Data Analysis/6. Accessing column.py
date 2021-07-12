# import pandas as pd
# presidents_df = pd.read_csv(
#     'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# print(presidents_df.columns)
##################################
# import pandas as pd
# presidents_df = pd.read_csv(
#     'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# writes all column with the name provided.
# print(presidents_df["height"])
##################################
# import pandas as pd
# presidents_df = pd.read_csv(
#     'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# print(presidents_df["height"].shape)  # writting shape of column height.
##################################
# import pandas as pd
# presidents_df = pd.read_csv(
#     'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# # using list to show multiple columns at a time.
# print(presidents_df[["height", "age"]])
##################################
# import pandas as pd
# presidents_df = pd.read_csv(
#     'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# # use list to show multiple columns at a time and number of rows to print.
# print(presidents_df[["height", "age"]].head(n=3))
##################################
import pandas as pd
presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# using "loc" to print data with rows and column size restricted.
print(presidents_df.loc[:, "height", "age"].head(n=3))
