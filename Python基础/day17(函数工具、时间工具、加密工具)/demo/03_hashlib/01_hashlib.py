'''
	账户：		laowang@qq.com			laowang@qq.com
	登录密码：	gebilaowang				234khkhwrk998y892h3i4hkhkhwkrhwr8h2k34hk32hr
	支付密码：	123321					skhksjhoiw329822oi3h4hkjshrkjshkdshfiudshsih
'''

import hashlib


pwd = '123456'
#md5加密的对象
m = hashlib.md5()
#将密码更新加密对象中
m.update(pwd.encode('utf-8'))
#生成长度32的16进制组成的字符串
pwd = m.hexdigest()
print(pwd)


'''
自学sha模块的加密
'''