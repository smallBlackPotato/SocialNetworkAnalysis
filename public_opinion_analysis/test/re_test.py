import re

str_text = "为这样的人伤心一点都不值得 😡说得对 👏还好你及时离开了他，要不然会伤的更深。罗志祥你可以对此做出一个解释吗？居然还有另一部📱用来聊妹。渣😡"

# # 找出@用户
# result_str = re.search(r'(?=@)\S+(\W)', str_text)

# str_text = re.sub(r'(?=@)\S+(\W)', " ", str_text, count=0, flags=0)

# print(result_str)
# print(result_str[0])
# print(str_text)


# 找出表情字符

pattern = re.compile(r'(\W)')        #查找表情
result_str_sign = pattern.findall(str_text)
print(result_str_sign)
for item in result_str_sign:
    print(item)

str_text = re.sub(r'(\W)', " ", str_text, count=0, flags=0)

print(str_text)
print(type(str_text))
