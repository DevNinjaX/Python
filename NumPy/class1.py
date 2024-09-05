# Creating array
import numpy as np

# direct array creating
a = np.array([1, 2, 3])
print(a)

# check dimensions of any array
print(f"Dimension of array {a.ndim}")

# list to array converting
x = [1, 2, 3]
y = np.array(x)
print(y)

# array element through user input 
l = []
for i in range(1, 4):
    ele = int(input("Enter element: "))
    l.append(ele)

arr = np.array(l)
print(arr)

# 2-D Array
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2)
print(f"Dimension of array {arr2.ndim}")

# 3-D Array
# arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]], [[1,2,3],[4,5,6],[7,8,9]]])
arr3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr3)
print(f"Dimension of array {arr3.ndim}")

# Higher Dimensional Array
arr4 = np.array([1, 2, 3], ndmin=5) # Using ndmin we also create 2-D and 3-D array
print(arr4)
print(f"Dimension of array {arr4.ndim}")