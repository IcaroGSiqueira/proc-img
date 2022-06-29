import numpy as np

m = np.random.randint(size=(5,5), low=-10, high=10)

print("original:\n", m)

# A

check_negative = m < 0

count_negative = np.sum(check_negative)

print("\nbusca negativos:\n", check_negative)
print("\nconta negativos:\n", count_negative)

# B

zeroed_negatives = m.copy()
zeroed_negatives[zeroed_negatives < 0] = 0

print("\nnegativos zerados:\n", zeroed_negatives)

# C

sum_positives = np.sum(zeroed_negatives)

print("\npositivos somados:\n", sum_positives)

# D

positives = zeroed_negatives.copy()[zeroed_negatives.copy() != 0]

average_positives = float("{:.2f}".format(positives.mean()))

print("\npositivos:\n", positives)
print("\nmédia dos positivos:\n", average_positives)