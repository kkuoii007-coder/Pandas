import pandas as pd

df = pd.read_csv('dz.csv')
print(df.head())
print('-----' * 10)
print(df.info())
print('-----' * 10)
print(df.describe())
print('-----' * 10)
group = df.groupby('City')['Salary'].mean()
print(group)