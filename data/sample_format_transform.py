"""
讀取csv檔,輸出parquet、json、excel、ORC
"""
import pandas as pd
from os.path import join

DirPath = r'.\sample'
filename = 'Iris.csv'

# read csv
df = pd.read_csv(join(DirPath, filename))
print(df)

# 輸出parquet
print('output parquet')
df.to_parquet(join(DirPath, '{}.parquet'.format(filename.split('.')[0])))
print(pd.read_parquet(join(DirPath, '{}.parquet'.format(filename.split('.')[0]))))

# 輸出 json
print('output json')
df.to_json(join(DirPath, '{}.json'.format(filename.split('.')[0])), orient="table", index=False)
# print(pd.read_parquet(join(DirPath, '{}.parquet'.format(filename.split('.')[0]))))

# 輸出excel
print('output excel')
df.to_excel(join(DirPath, '{}.xlsx'.format(filename.split('.')[0])), sheet_name='Sheet_1', index=False)
print(pd.read_excel(join(DirPath, '{}.xlsx'.format(filename.split('.')[0]))))

# 輸出ORC
print('output ORC')
df.to_orc(join(DirPath, '{}.orc'.format(filename.split('.')[0])))
# print(pd.read_orc(join(DirPath, '{}.orc'.format(filename.split('.')[0]))))