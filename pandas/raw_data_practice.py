# data cleaning
import pandas as pd
pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)# to see all rows
df=pd.read_csv("C:/Users/hi/.vscode/py/python/pandas/raw_data @Skillshala90.csv")
# ##Handle  duplicates
# print(df.duplicated())
# print(df["country"].duplicated())
# print(df)
# print(df[["country","gender"]].duplicated())
# print(df.drop_duplicates())# they not chamge actual data & old labbel is show
# print(df["name"] )
# df2=df.copy()#copy for future use
# df.drop_duplicates(inplace=True)# it delete form original data
# print(df)
# df=df2#backtrack the data
# print(df)

### Data types
# df2=df.copy()

# df2=df2.fillna(0)  # cannot convert nan data into int
# print(df2)
# df2["age"]=df2["age"].astype("int64").copy()
# print(df2.dtypes)


# date_str=pd.Series([pd.to_datetime("2026-12-31")])
# print(type(date_str.dtypes))##  string--->date time data change


# pd.set_option('display.max_columns',None)
# # pd.set_option('display.max_rows',None)# to see all rows
# aqi_data=pd.read_csv("C:/Users/hi/Downloads/archive.zip")
# print(aqi_data.columns)
# print(aqi_data["timestamp"].dtypes)
# aqi_data["timestamp"]=pd.to_datetime(aqi_data["timestamp"])
# print(aqi_data["timestamp"].dtype)


####### string
# print(df["gender"].str.lower())
# print(df["gender"].str.upper())
# print(df["gender"].str.capitalize())
# print(df["gender"].str.strip())## remove spaces
# print(df["name"].str.split(" "))# # split through space
# print(df["country"].str.contains("US"))
# print(df["country"].str.contains("INDIA",case=False))# ignore case A&a
# # anuj@gmail.com # use split("@")


####################Feature engg. 
#Transforming data
df2=df.copy()
# df2["tax"]=df2["income"].apply(lambda x: "20%" if x>=50000 else "10%")
# print(df2)
# we want to create male-->M ,feamale-->F, UNKNOWN-->U
# gender_map={"Male":"M","Female":"F","Unknown":"U"}
# print(df2["gender"].map(gender_map))
# df2["gender"]=df2["gender"].map(gender_map)# to permanent change in df2
# print(df2)
# print(df2.assign(new_income=df2["income"] *1.1) ) #10/100=1.1
df2=df2.assign(new_income=df2["income"] *1.1)
# print(df2["country"].replace("USA","US"))
# df2["country"]=df2["country"].replace("USA","United State")
# print(df2)

df2.columns=["ID","NAME","Age","Country","Gender","Income","New_Income"]
# print(df2.rename(columns={"Income":"Salary"}))
# print(df2.rename(index={1:"First"}))
# print(df2.sort_values("Income"))
# print(df2.sort_values("Income",ascending=False))
# df2=df2.fillna(50)
# print(df2.sort_values(["Income","Age"]))#comapre income than Age
sorted_df=df2.sort_values(["Income","Age"])
# print(sorted_df.sort_index())
###reset
# print(sorted_df.reset_index())
# print(sorted_df.reset_index(drop=True))
## Ranking
# sorted_df["Ranking"]=sorted_df["Income"].rank()
# print(sorted_df) ## if income same than rank=avg((4+5)/2=4.5 assighn)
# sorted_df["Ranking"]=sorted_df["Income"].rank(ascending=False)#decending order
# sorted_df["Ranking"]=sorted_df["Income"].rank(ascending=False,method="dense")##method="First",method="max"(maxno. assign both )
# print(sorted_df)
print(sorted_df[["ID","NAME","Age","Country","Gender","New_Income","Income"]])
