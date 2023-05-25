import pandas as pd
df=pd.read_csv("nisar.csv")
print(df)
d=pd.isnull(df)
x=df["Age"].mean()
df=df.fillna(x)
print(df)
