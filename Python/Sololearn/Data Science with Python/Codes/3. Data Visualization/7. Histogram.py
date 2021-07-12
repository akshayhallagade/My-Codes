# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# presidents_df = pd.read_csv(
#     'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
# presidents_df["height"].plot(kind="hist", title="height", bins=5)
# plt.savefig("3. Data visualization/fig6.png")
# plt.show()
###################### OR #########################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
presidents_df = pd.read_csv(
    'https://sololearn.com/uploads/files/president_heights_party.csv', index_col='name')
plt.hist(presidents_df['height'], bins=5)
plt.savefig("3. Data visualization/fig6.png")
plt.show()
