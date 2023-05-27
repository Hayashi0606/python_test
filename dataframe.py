import pandas as pd
series_1 = pd.Series(dict(a=1, b=2, c=3, d=4, e=5))
series_2 = pd.Series(dict(a=11, b=12, c=13, d=14, e=15))
df = pd.DataFrame({'column_1': series_1, 'column_2': series_2})
print(df) 
data = df['column_2'][2]
print(data)