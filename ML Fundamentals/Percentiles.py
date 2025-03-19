import numpy as np
import matplpotlib.pyplot as plt


data = [12,14,18,20,16]
p_25 = np.percentile(data, 25)
p_50 = np.percentile(data, 50)
p_75 = np.percentile(data, 75)

print(f"25th Percentile: {p_25}")
print(f"50th Percentile (Median): {p_50}")
print(f"75th Percentile: {p_75}")


