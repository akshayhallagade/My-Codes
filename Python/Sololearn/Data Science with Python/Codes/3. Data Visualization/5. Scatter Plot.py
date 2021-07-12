# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# presidents_df = pd.read_csv(
#     'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# plt.scatter(presidents_df["height"], presidents_df["age"])
# plt.savefig("3. Data visualization/fig4.png")
# plt.show()
#############################################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
plt.scatter(presidents_df["height"],
            presidents_df["age"], marker="<", color="k")
plt.xlabel("height")
plt.xlabel("age")
plt.title("U.S. presidents")
plt.savefig("3. Data visualization/fig4.png")
plt.show()
