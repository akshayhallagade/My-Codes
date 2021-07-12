import pandas as pd
presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')  # read
print(presidents_df.shape)  # shape
print(presidents_df.shape[0])  # shape
print(presidents_df.size)  # size
print(presidents_df.head(n=3))  # head : writes top 3 rows. n(default)=5
print(presidents_df.tail())  # tail : writes bottom 5 rows. n(default)=5
# info : gives overview of dataframe. includes (index, column, names, dtype, and memory usage.)
print(presidents_df.info())
