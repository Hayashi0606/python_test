import pandas as pd
data = [[1, 2, 3], [11, 12, 13]]
df = pd.DataFrame(data, index=['a', 'b'], columns=['col_1', 'col_2', 'col_3'])
print(df)