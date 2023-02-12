import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('EV_dataset - Sheet1.csv')
df.dropna(inplace =  True)
print(df.to_string)
print(df.corr())


sns.regplot(df['Affordability'],df['Profitability'])

sns.regplot(df['Profitability'],df['Monthly payment'])




df.columns
df.Affordability.hist()


df.Sales.hist()


df.Profitability.hist()
