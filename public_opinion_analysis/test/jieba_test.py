import jieba,math

# str_text = '竟然。。。。。'
str_text = '为这样的人伤心一点都不值得说得对 还好你及时离开了他 要不然会伤的更深 罗志祥你可以对此做出一个解释吗 居然还有另一部 用来聊妹 渣'

#精准模式cut_all=False，默认即是
str_jing1=jieba.cut(str_text,cut_all=False)
print('精准模式分词：{ %d}' % len(list(str_jing1)))
str_jing2=jieba.cut(str_text,cut_all=False)

print(type(str_jing2))

print("/".join(str_jing2))

b = "/".join(str_jing2)

print(type(b))