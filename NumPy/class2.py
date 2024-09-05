# create Numpy array using Numpy function
import numpy as np

# Array filled with 0's
arr_zero = np.zeros(4) # 1-D array
print(arr_zero)

arr_zero2 = np.zeros((3,3)) # 2-D array
print(arr_zero2)

arr_zero3 = np.zeros((5,5)) # 5-D array
print(arr_zero3)

# Array filled with 1's
arr_one = np.ones(4) # 1-D array
print(arr_one)

arr_one2 = np.ones((3,3)) # 2-D array
print(arr_one2)

arr_one3 = np.ones((5,5)) # 5-D array
print(arr_one3)

# create an empty array
arr_emp = np.empty(4) # In an empty array the previous memory of an array will be stored otherwise it shows memmory address
print(arr_emp)

# An array with a range of elements
arr_rn = np.arange(4) # example 1
print(arr_rn)

arr_rn2 = np.arange(5,10) # example 2
print(arr_rn2)

# Array diagonal element filled with 1's
arr_dl = np.eye(1) # 1-D array
print(arr_dl)

arr_dl2 = np.eye(2) # 2-D array
print(arr_dl2)

arr_dl3 = np.eye(3) # 3-D array
print(arr_dl3)

arr_dl4 = np.eye(3, 5) # 3:5 array
print(arr_dl4)

# Create an array with values that are spaced linearly in a specified interval
arr = np.linspace(0,10,num=5) # exaple 1
print(arr)

arr = np.linspace(0,20,num=5) # exaple 2
print(arr)