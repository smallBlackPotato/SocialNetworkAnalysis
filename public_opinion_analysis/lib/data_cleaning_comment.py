import pandas as pd
import numpy as np
import jieba,math
import re

open_data = pd.read_csv("data/Result_id.csv", index_col = False)

# print(open_data.at[111830, '评论'])

for row_index, row in open_data.iterrows():
    # print(row_index, open_data.at[row_index, '评论'])
    

