import numpy as np
import pandas as pd
# we can use list to create an pandas Series.
print(pd.Series([1, 2, 3], index=["a", "b", "c"]))
# we can use numpy array to create an pandas Series.
print(pd.Series(np.array([1, 2, 3]), index=["a", "b", "c"]))
# we can use numpy dictionary to create an pandas Series.
print(pd.Series({"a": 1, "b": 2, "c": 3}))
