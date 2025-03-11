import math

data = [12,18,14,20,16]

mean = sum(data) / len(data)
variance = sum((x - mean) ** 2 for x in data) / len(data)
std_deviation = math.sqrt(variance)

print(f"Standard Deviation: {std_deviation}")