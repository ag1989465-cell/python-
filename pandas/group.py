import pandas as pd
pd.set_option('display.max_columns',None)
df=pd.read_csv("C:/Users/hi/.vscode/py/python/pandas/raw_data @Skillshala90.csv")
df2=df.copy()
# df2=df2.groupby("country")["income"].mean()
# df2=df2.groupby("country")["income"].min()
# df2=df2.groupby("country")["income"].max()
# df2=df2.groupby("gender")["income"].max()
# print(df2)

# df2=df2.groupby("gender")["income"].agg(["mean","min","max"])
# df2=df2.groupby("gender")["income"].aggregate(["mean","min","max"])  # same as upper one
# df2=df2.groupby("country")["income"].agg([avg_salary="mean",min_salary="min",max_salary="max"])
# print(df2)
# df2=df.groupby("country").agg({
#     "income" :"mean",
#     "age":"max"
# })
# print(df2)
# df2=df.groupby("country").agg(
#     mean_salary=("income" ,"mean"),
#     max_salar=("age","max"),
#     min_salary=("income","min")
# )
# print(df2)


###########         melt(wide to long format) & pivot(Long to wide format)
#melt(id_vars(#keep),value_vars(unpivot),var_name(new_col name),value_name(new_col value))
# df=pd.DataFrame({
#     "country":["USA","USA","INDIA","INDIA"],
#     "year":[2020,30032,4343,2022],
#     "sales":[100,120,90,110],
#     "profit":[20,25,18,22],
#     # "tax":[10,20,30,40]
# })
# # print(df)
# melted_df=df.melt(
#     id_vars=["country","year"],
#     # value_vars=["sales","profit","tax"],
#         value_vars=["sales","profit"],
#     var_name="metrics",
#     value_name="value"
# )
# print(melted_df)
# #######  pivot(index(keep),columns,values)
# original=melted_df.pivot(
#     index=["country","year"],
#     columns="metrics",
#     values="value"

# )
# print(original)

###### data visualisation
df=pd.read_csv("C:/Users/hi/.vscode/py/python/pandas/employee_data.csv")# try in anconda
print(df["Age"].hist())# try in anconda
print(df.plot(kind="scatter",x="Age",y="Salary"))# try in anconda
