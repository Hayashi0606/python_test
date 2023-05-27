import pandas as pd

df = pd.DataFrame([[1, 2], [11, 12], [21, 22]], index=['a', 'b', 'c'], columns=['column_1', 'column_2'])
print(df.iloc[[0, 2], [0, 1]])
df.iloc[[1, 2], [0, 1]] = [[1001, 1002], [1003, 1004]]
print(df)