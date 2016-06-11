import hashlib

pwd = '123456'
my_md5 = hashlib.md5()
my_md5.update(pwd.encode('utf-8'))
ret = my_md5.hexdigest()
print(ret)


pwd = '123456'
my_sha1 = hashlib.sha1(pwd.encode('utf-8'))
ret = my_sha1.hexdigest()
print(ret)