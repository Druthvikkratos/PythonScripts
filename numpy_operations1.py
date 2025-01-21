import numpy as np

arr1 = np.array([1,2,3])
print(arr1)
arr2 = np.array([[1,2],[3,4]])
print(arr2)
print(f" Shape Of Array: {arr2.shape}")
print(f"Number Of Dimesions: {arr2.ndim}")
print(f"Total Number Of Elements: {arr2.size}")
print(f"Data Type Of Elements: {arr2.dtype}")

zeros = np.zeros((2,3))
ones = np.ones((3,4))
empty = np.empty((2,3))
identity = np.eye(3)
print(f" Zeros: {zeros}")
print(f"Ones: {ones}")
print(f"Empty: {empty}")
print(f"Identity: {identity}")

#Create a 3x3 array of random numbers and replace all elements 
# greater than 0.5 with 1, and others with 0.
random = np.random.rand(3,3)
print(np.where((random > 0.5) & (random != 1), 1, 0))

#Initialize a 5x5 array with all ones on the border and zeros inside.
ones = np.ones((5,5))
ones[1:-1, 1:-1] = np.full((3,3), 0)
print(ones)