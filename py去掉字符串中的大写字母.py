


# 删除字符串中的大写字母
import re
s = 'ThiS iS A PyTHon StrinG witH SomE CAPitaL LettErs'
print(re.sub(r'[A-Z]', '', s))


s2 = ''.join(ch for ch in s if not ch.isupper())
print(s2)


# 输出结果。
# #----------------------------------------------------------------
# hi i  yon trin wit om ita ettrs
# hi i  yon trin wit om ita ettrs