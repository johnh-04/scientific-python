# Numpy is a powerful library for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.

# pip install numpy

import numpy as np

# Creating a numpy array
list = [1, 2, 3, 4, 5]
arr = np.array(list)
print(arr)  # Output: [1 2 3 4 5]
print(type(arr))    # Output: <class 'numpy.ndarray'>

# Creating a numpy array with a specific data type
arr_float = np.array(list, dtype=float)
print(arr_float)  # Output: [1. 2. 3. 4. 5.]
print(arr_float.dtype)  # Output: float64

# Creating a numpy matrix
list_2d = [[1, 2, 3], [4, 5, 6]]
matrix = np.array(list_2d)
print(matrix)  # Output: [[1 2 3] [4 5 6]]
print(type(matrix)) # Output: <class 'numpy.ndarray'>

# Special arrays
zeros_array = np.zeros((3, 3))
print(zeros_array)  # Output: [[0. 0. 0.] [0. 0. 0.] [0. 0. 0.]] (array filled with 0s of shape 3x3)
ones_array = np.ones((2, 4))
print(ones_array)  # Output: [[1. 1. 1. 1.] [1. 1. 1. 1.]] (array filled with 1s of shape 2x4)
eye_array = np.eye(4)
print(eye_array)  # Output: [[1. 0. 0. 0.] [0. 1. 0. 0.] [0. 0. 1. 0.] [0. 0. 0. 1.]] (identity matrix of size 4x4)
full_array = np.full((2, 3), 7)
print(full_array)  # Output: [[7 7 7] [7 7 7]] (array filled with 7s of shape 2x3)

# Ranges
range_array = np.arange(0, 10, 2)
print(range_array)  # Output: [0 2 4 6 8] (range of numbers from 0 to 10 with a step of 2)
linspace_array = np.linspace(0, 1, 5)
print(linspace_array)  # Output: [0. 0.25 0.5 0.75 1.] (5 evenly spaced numbers between 0 and 1)

# Array properties
print(matrix.shape)  # Output: (2, 3) (number of rows, number of columns)
print(matrix.ndim)  # Output: 2 (number of dimensions)
print(matrix.size)  # Output: 6 (total number of elements)
print(matrix.dtype)  # Output: int64 (data type of elements)

# Random arrays
random_array = np.random.rand(3, 3)
print(random_array)  # Output: A 3x3 array of random numbers between 0 and 1
random_int_array = np.random.randint(0, 10, (4, 4))
print(random_int_array)  # Output: A 4x4 array of random integers between 0 and 10

# Mathematical and Matrix operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # Output: [5 7 9] (element-wise addition)
print(a - b)  # Output: [-3 -3 -3] (element-wise subtraction)
print(a * b)  # Output: [4 10 18] (element-wise multiplication)
print(a / b)  # Output: [0.25 0.4 0.5] (element-wise division)
print(a ** 2)  # Output: [1 4 9] (element-wise exponentiation)

print(a.dot(b))  # Output: 32 (dot product)
print(np.dot(a, b))  # Output: 32 (dot product using numpy function)
print(a @ b)  # Output: 32 (dot product using operator)

print(a.T)  # Output: [1 2 3] (transpose of a, which is the same since it's a 1D array)

# Indexing and slicing
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])  # Output: 10 (first element)
print(arr[-1])  # Output: 50 (last element)

print(arr[1:4])  # Output: [20 30 40] (slicing from index 1 to 3)
print(arr[:2])  # Output: [10 20] (slicing from index 0 to 1)
print(arr[::-1])  # Output: [50 40 30 20 10] (reversing the array)

# Statistical functions
data = np.array([1, 2, 3, 4, 5])
print(np.sum(data))  # Output: 15 (sum of all elements)
print(np.mean(data))  # Output: 3.0 (mean of the elements)
print(np.median(data))  # Output: 3.0 (median of the elements)
print(np.std(data))  # Output: 1.4142135623730951 (standard deviation of the elements)
print(np.min(data))  # Output: 1 (minimum value)
print(np.max(data))  # Output: 5 (maximum value)
print(np.percentile(data, 25))  # Output: 2.0 (25th percentile)
print(np.percentile(data, 75))  # Output: 4.0 (75th percentile)
print(np.var(data))  # Output: 2.0 (variance of the elements)
print(np.corrcoef(data, data))  # Output: [[1. 1.] [1. 1.]] (correlation coefficient between data and itself)
print(np.cov(data, data))  # Output: [[2.5 2.5] [2.5 2.5]] (covariance between data and itself)

# Universal functions
arr = np.array([0, np.pi / 2, np.pi])
print(np.sin(arr))  # Output: [0. 1. 0.] (sine of each element)
print(np.cos(arr))  # Output: [1. 0. -1.] (cosine of each element)
print(np.exp(arr))  # Output: [ 1.  4.81047738e+00  2.31881573e+00] (exponential of each element)
print(np.log(arr + 1))  # Output: [0. 0.88137359 1.09861229] (natural logarithm of each element)
print(np.sqrt(arr))  # Output: [0. 1.25331414 1.77245385] (square root of each element)
print(np.abs(arr - np.pi / 2))  # Output: [1.57079633e+00 0.00000000e+00 1.57079633e+00] (absolute value of the difference from pi/2)
print(np.round(arr, decimals=2))  # Output: [0. 1.57 3.14] (rounding each element to 2 decimal places)
print(np.floor(arr))  # Output: [0. 1. 3.] (floor of each element)
print(np.ceil(arr))  # Output: [0. 2. 3.] (ceiling of each element)
print(np.sign(arr - np.pi / 2))  # Output: [-1. 0. 1.] (sign of the difference from pi/2)
print(np.where(arr > np.pi / 2, "greater", "not greater"))  # Output: ['not greater' 'not greater' 'greater'] (conditional selection based on the condition)
print(np.unique(arr))  # Output: [0. 1.57079633 3.14159265] (unique elements in the array)

# Write and Read from files
arr = np.array([[1, 2, 3], [4, 5, 6]])

np.savetxt("array.txt", arr, delimiter=",")
loaded_arr = np.loadtxt("array.txt", delimiter=",")
print(loaded_arr)  # Output: [[1. 2. 3.] [4. 5. 6.]] (array loaded from the file)

np.save("array.npy", arr)
loaded_arr_npy = np.load("array.npy")
print(loaded_arr_npy)  # Output: [[1 2 3] [4 5 6]] (array loaded from the .npy file)