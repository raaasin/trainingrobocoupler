import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("nisar.csv")
x=df["Age"]
plt.boxplot(x)
plt.show()
print(df.max())
df=df.replace(200,20)
print(df)
