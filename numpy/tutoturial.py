import time
import numpy as np
# execution time of a code performance
size=1_000_000
py_list=range(size)
start=time.time()
sq_list=[x**2 for x in py_list]
end=time.time()
print("Python list took",end-start,"seconds")

#numpy array
np_array=np.array(py_list)
start=time.time()
end=np_array**2
end=time.time()
print("NumPy array took",end-start,"seconds")

# memory size
import sys
print ("Python list size in bytes:",sys.getsizeof(py_list)*len(py_list))
print ("NumPy array size in bytes:",np_array.nbytes)