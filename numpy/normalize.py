# #normalize
# import numpy as np
# arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(np.mean(arr))
# print(np.std(arr))#standard deviation
# normalized_arr=(arr-np.mean(arr))/np.std(arr)
# print(normalized_arr)#mean=0 and std=1


# mathematical functions
import numpy as np
arr=np.array([1,2,3,4,5])
print("square root =",np.sqrt(arr))#square root
print("natural log",np.log(arr))#natural logarithm
print("exponential",np.exp(arr))#
print("sum of all elements",np.sum(arr))#
print("product of all elements",np.prod(arr))#
print("minimum element",np.min(arr))#
print("#maximum element",np.max(arr))  
print("index of minimum element",np.argmin(arr))#"index of minimum element"
print("index of maximum element",np.argmax(arr))#
print("mean od the aray",np.mean(arr))
print("median of the array",np.median(arr))
print("standard deviation",np.std(arr))
print("variance",np.var(arr))#variance
print(np.square(arr))
print(np.log(arr))
print(np.log2(arr))#log base 2
print(np.exp(arr))#exponent
print(np.round(3.94))    # round up
print(np.ceil(3.14))    
print(np.floor(3.14))    
print(np.trunc(3.14))
arr=np.array([1,2,3,4,5,6,7,2,3,])    
print(np.unique(arr))        
print(np.sort(arr))
print(np.abs(arr))
                