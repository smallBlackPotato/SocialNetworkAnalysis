import pandas as pd
import numpy as np
import jieba,math
import jieba.analyse

# open_data = pd.read_csv("data/datas.csv", index_col = False, names = ['用户微博','id','用户名','评论','回复','获赞','时间','回复URL'])
open_data = pd.read_csv("data/datas.csv", index_col = False)

# print(open_data['评论'].iloc[1:2])
# print(type(open_data['评论'].iloc[1:2]))

print(open_data.at[1,'评论'])
str_text = open_data.at[1,'评论']
# print(type(open_data.at[1,'评论']))

# print(open_data.loc[1, '评论'])#根据行列标签
# print(open_data.iloc[1, 3])#根据行列编号


#精准模式cut_all=False，默认即是
str_jing1=jieba.cut(str_text,cut_all=False)
print('精准模式分词：{ %d}' % len(list(str_jing1)))
str_jing2=jieba.cut(str_text,cut_all=False)
print("/".join(str_jing2))

str_test = jieba.lcut(str_text,cut_all=False)
print(type(str_test))
print("/".join(str_test))
print("***")
b = "/".join(str_test)
print(b)
print("***")
for item in str_test:
    print(item)



# str_jing1=jieba.cut(str_text,cut_all=False)
# print("/".join(str_jing1))
# print('精准模式分词：{ %d}' % len(list(str_jing1)))
# print(type(str_jing1))
# print(str_jing1)
# str_jing2=jieba.cut(str_text,cut_all=False)
# print(str_jing2)
# # print("/".join(str_jing1))
# print("/".join(str_jing2))
# s = "/".join(str_jing2)
# print(s)