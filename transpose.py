#Transpose with Zip
#Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this!.
import numpy as np

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose =np.array([list(i) for i in data]).transpose()
print(data_transpose)
