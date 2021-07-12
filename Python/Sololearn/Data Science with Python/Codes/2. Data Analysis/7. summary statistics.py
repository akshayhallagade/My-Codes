"""................Measure of Location................

This are the quantities that represent the average value of a variable.

ex : Minimum, Maximum, Mean"""
# .....................................................
""".................Measure of Spread...................

It represent how similar or dissimilar the values of a variable are.

ex. Range, Variance, Standard Deviation"""
###################################################################

# import pandas as pd
# presidents_df = pd.read_csv(
#     'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# # writes minimum of column.
# print(presidents_df.min())
# #############################################
# import pandas as pd
# presidents_df = pd.read_csv(
#     'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# # writes maximum of column.
# print(presidents_df.max())
# #############################################
import pandas as pd
presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# writes average of each column.
print(presidents_df.mean())
#############################################
