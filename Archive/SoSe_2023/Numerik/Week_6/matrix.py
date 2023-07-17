import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])  # 2x3 matrix
b = np.array([[1, 2], [3, 4], [5, 6]])  # 3x2 matrix

print(a)
print(b)
print(np.matmul(a, b))
print(np.linalg.inv(np.matmul(a, b)))
print(a.transpose())
print(np.linalg.det(np.matmul(a, b)))
