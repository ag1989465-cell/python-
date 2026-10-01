# import numpy as np

# # Creating a 2D NumPy array
# arr = np.array([[1, 2, 3],
#                 [4, 2, 5]])

# print("Array type:", type(arr))
# print("Number of dimensions:", arr.ndim)
# print("Shape:", arr.shape)
# print("Size:", arr.size)
# print("Element data type:", arr.dtype)
# import numpy as np
# arr=np.array([3,6,777,8],np.int8) 
# print(arr)
import numpy as np
# arr=np.array([[3,6,777,8,7],[1,4,6,7,9]],np.int32) 
# print(arr[0])
# print(arr.shape)
# print(arr.dtype)
# print(arr.size)

arr=np.array({34,23,45,67,89})
print(arr)
print(arr.dtype)

arr=np.zeros((2,5),np.int32)
print(arr)
print(arr.dtype)
print(arr.size)
print(arr.shape)

# x=np.arange(15)
# print(x)
# lspace=np.linspace(1,5,10)
# print(lspace)
# x=np.empty((3,4))
# print(x)
# y=np.eye(5)
# print(y)
# z=np.empty_like(lspace)
# print(z)
# print(np.identity(5))
# x=np.arange(28)
# # print(x)
# # print(x.reshape(2,7,2))
# # print(x.reshape(2,14))
# x=x.reshape(2,14)
# print(x)
# x=x.ravel()
# print(x)
