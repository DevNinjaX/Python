#Create numpy arrays with random numbers
import numpy as np

# rand(): the function is used to generate a random value between 0 to 1.
arr = np.random.rand(5)
print(arr)

arr2 = np.random.rand(2,3)
print(arr2)

# randn(): the function is used to generate a random value close to zero. This way return positive or negative numbers as well.
arr3 = np.random.randn(5)
print(arr3)

# ranf(): the function for doing random sampling in numpy. It returns an array of specified shape and fills it with random floats in the half-open interval [0.0, 1.0). [0.0, 1.0) means it include 0 but not 1.
arr3 = np.random.ranf(5)
print(arr3)

# randint(): the function is used to generate a random number within a given range.
arr4 = np.random.randint(10, 20, 5) # (min_value, maxx_value, total_value)
print(arr4)