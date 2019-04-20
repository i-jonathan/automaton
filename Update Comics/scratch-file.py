import pandas as pd
df = pd.read_csv('Update Comics/getcomics.csv', index_col='Index')
print(df)
df.to_csv('Update Comics/getcomics.csv')
