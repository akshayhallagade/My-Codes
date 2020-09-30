import numpy as np
my_list = [1, 2, 3, 4, 5, 6]
print(my_list)

array = np.array(my_list, dtype=int)
print(array)
print(type(array))
print(array.reshape(3, 2))
