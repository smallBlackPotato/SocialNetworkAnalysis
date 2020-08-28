import pandas as pd
import numpy as np
# import jieba,math

open_data = pd.read_csv("data/datas.csv", index_col = False)

# print(open_data)

# 删除指定列中有空值的行
open_data.dropna(subset=['评论'],inplace=True)
# 删除指定列（不改变open_data）
# open_data.drop(columns = ['回复URL'])

open_data = open_data.drop(labels='回复URL',axis=1)

# print(open_data)

# print(str(open_data.at[1,'id']))

# str_test = str(open_data.at[1,'id'])
# print(str_test.split("=")[1])


# print(open_data.head())

for row_index, row in open_data.iterrows():
    # 将id提取出来
    str_id = row['id'].split("=")[1]
    # 替换原来的id
    open_data.at[row_index,'id'] = str_id  
    # print(row_index,str_id)

# print(open_data.head())
# print(open_data.at[111852,'评论'])

open_data.to_csv('data/Result_id.csv', index=None, encoding="utf_8_sig")
# print(open_data)
