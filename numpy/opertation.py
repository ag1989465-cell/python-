# import numpy as np
# arr=np.array([[1, 2, 3],[4, 5, 6]])
# print(arr,arr.shape)

# reshaped_arr=arr.reshape(3,2)
# print(reshaped_arr,reshaped_arr.shape)

# flattened_arr=arr.flatten()
# print(flattened_arr,flattened_arr.shape)

# import numpy as np
# arr1=np.array([[1, 2, 3],[4, 5, 6]])
# print(arr1[0, 1])  # Accessing element at row 0, column 1
# print(arr1[0][1])# Accessing element at row 0, column 1
# # arr1[0, 1] = 10  # Modifying element at row 0, column 1
# # print(arr1)  # Printing the modified array

## fancy indexing
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# # Accessing elements using fancy indexing
# idx=[0,1,3]
# print(arr[idx])  # Accessing the first row

# # bollean indexing
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# # Accessing elements using boolean indexing
# mask = arr > 5
# print(arr[mask])  # Accessing elements greater than 5
# print(arr[arr%2 == 0])  # Accessing even elements

#slicing
# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# # Accessing a subarray using slicing
# print(arr[0:2, 1:3])  # Accessing rows 0 to 1 and columns 1 to 2


# #copying array vs view
# import numpy as np
# nums=[1,2,3,4,5]
# sub_list=nums[1:3]
# print(sub_list)
# sub_list[0]=10
# print(sub_list)
# print(nums)

# arr=np.array([1, 2, 3, 4, 5])
# # Creating a view of the array
# sub_arr = arr[1:3]
# print(sub_arr)  # Output: [2 3]
# sub_arr[0] = 10
# print(sub_arr)  # Output: [10  3]
# print(arr)  # Output: [ 1 10  3  4  5] (original array is modified)


# import numpy as np
# arr=np.array([1, 2, 3, 4, 5])
# # Creating a copy of the array
# sub_arr_copy = arr[1:3].copy()
# print(sub_arr_copy)  # Output: [2 3]
# sub_arr_copy[0] = 10
# print(sub_arr_copy)  # Output: [10  3]
# print(arr)  # Output: [ 1  2  3  4  5] (original array is not modified)


# complex number
# import numpy as np
# arr = np.array([1 + 2j, 3 + 4j, 5 + 6j])
# arr2 = np.array([1 + 2j, 3 + 4j,5 + 6j])
# # Accessing the real and imaginary parts of the complex numbers
# print("Real parts:", arr.real)  # Output: [1. 3. 5.]
# print("Imaginary parts:", arr.imag)  # Output: [2. 4. 6.]
# arr3=np.array([arr+arr2],dtype=complex)  
# print("Sum:", arr3)  # Output: [ 2.+4.j  6.+8.j 10.+12.j]

import numpy as np
arr= np.array(["PRICE",{1,2,3},3.14])
print(arr,arr.dtype)  # Output: ['PRICE' {1, 2, 3} 3.14] object