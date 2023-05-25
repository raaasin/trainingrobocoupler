import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
df = pd.read_csv("nisar.csv")
sns.pairplot(df)
plt.show()
