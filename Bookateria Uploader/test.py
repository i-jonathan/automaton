import os
import pandas as pd

df = pd.read_csv('/media/jay/Files/Documents/Projects/Pyprojects/Selenium/Bookateria Uploader/bookateria-uploader.csv', index_col='Index')

for i in range(len(df)):
    path = str(df.Path[i])
    exists = os.path.isfile(path)
    if not os.path.isfile(path):
        print(path)