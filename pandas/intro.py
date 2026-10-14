#sereis= 1D labelled array
# Dataframe=2d labelled array 
# import pandas as pd
# info={
#     "Name":["Amuj","harshita","Ansh"],
#     "CGPA":[9.5,7.5,3.2]
# }
# df=pd.DataFrame(info)
# print(df)

# import pandas as pd
# s=pd.Series([1,2,3,45,6,57,8,9,10])
# print(s)
# print(type(s))
# #index
# print(s[0])
# print(s[2])

# import pandas as pd
# s=pd.Series([23,52,41,6,3],index=["Adam","Eva","Bob","Charlie","Anuj"])
# print(s)
# print(s["Adam"])
# print(s.iloc[0])
# print(s.index)


### series (properties)
#1.Homogenous
# 2.Vectorized
# 3.Handle Missing values with NaN
# 4.Mutable Values ,immutable size

import pandas as pd
s1=pd.Series([1,2,3,4,5])
s2=pd.Series([10,20,30,40,50])
print(s1+s2)
s1[0]=100
print(s1)
change=s1.drop(0)
print(s1)# immutable
print(change)