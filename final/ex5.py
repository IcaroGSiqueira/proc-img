import math
import numpy as np
from scipy.spatial import distance

n = 101
m = np.random.randint(0, 99999, size=(n,n))
center = math.ceil(n/2)
print(center)

for i in range(len(m)):
    for j in range(len(m[0])):
      dist = distance.euclidean(m[i][j], m[center][center])
      print(dist)