# aqi data set
import pandas as pd
pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)# to see all rows
df=pd.read_csv("C:/Users/hi/Downloads/archive.zip")
# print(df.describe())

#selecting data from column name
# print(df["city"])
# print(df[["city","aqi"]])
# # selecting  rows
# when we acess data from label--->loc
# when we acess data from index--->iloc
# print(df.loc[0])
# print(df.loc[0:2])#ending index inclusive(2 is include)

# print(df.iloc[0])
# print(df.iloc[0:2]) #ending index exclusive(2 is exclude)

#cells--row ,col
# print(df.loc[0,"aqi"])
# print(df.loc[0:2,["city","aqi"]])

# print(df.columns)
# print(df.iloc[0:2,2])
# print(df.iloc[0:2,[2,11]])

#cell
# print(df.at[0,"city"])
# print(df.iat[0,2])


# print(df["city"])#view
# cities=df["city"].copy()#copy
# cities[0]="Mumbai"
# print(df["city"])
# # print(df)


# ########## filtering
#  AND--->& or---->|  not-->~(bolleon value)
# print(df[df["aqi"]>100])
# print(df[(df["aqi"]>100) & (df["temperature"]>30)])

# print(df[df["aqi"]>100][["city","aqi"]])
# aqi_data=df[(df["aqi"]>100) & (df["temperature"]>30)][["city","aqi"]]
# print(aqi_data)
# print(aqi_data.iloc[0])
# print(aqi_data.loc[0]) # 0 labled are not here


# Query method----->copy
# print(df.query("aqi >100"))
# print(df.query("aqi >100 & temperature >30")[["city","aqi"]])
# aqi_val=100 # how to  use varibale in "@" use
# print(df.query("aqi > @aqi_val & temperature >30")[["city","aqi"]])


