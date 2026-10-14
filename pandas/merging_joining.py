######## merging and joining data
import pandas as pd 
df_customer=pd.DataFrame({
    "customer_id":[1,2,3,4],
    "name":["Adam","BOb","Charlie","Dave"]
})
df_order=pd.DataFrame({
    "order_id":[101,102,103,104],
    "customer_id":[2,1,4,5],
    "amount":[250,120,300,100]
})
# print(df_customer)
# print(df_order)
# print(pd.merge(df_customer,df_order,on="customer_id"))  ###inner join
# print(pd.merge(df_customer,df_order,on="customer_id",how="left"))## left join
# print(pd.merge(df_customer,df_order,on="customer_id",how="right"))#right join
# print(pd.merge(df_customer,df_order,on="customer_id",how="outer"))# outer join


############ concation
df1=pd.DataFrame({
    "id":[1,2,3],
    "name":["Adam","BOb","Charlie"]
})
df2=pd.DataFrame({
    "id":[4,5,6],
    "name":["Anuj","adarsh","ansh"]
})
print(pd.concat([df1,df2]),"\n")# row wise concation
print(pd.concat([df1,df2],ignore_index=True),"\n")
print(pd.concat([df1,df2],axis=1),"\n")#col wise