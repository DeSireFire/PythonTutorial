import os

print(os.path)
print(os.name)
print(os.sep)

path = 'a/b/c'

path = 'a%sb%s'%(os.sep,os.sep)
print(path)


print(os.linesep)


'''
rename
重命名文件或者文件夹
'''
src = r'C:\Users\Administrator\Desktop\老王.txt'
dst = r'C:\Users\Administrator\Desktop\laowang.txt'


src = r'C:\Users\Administrator\Desktop\cba'
dst = r'C:\Users\Administrator\Desktop\abc'
#os.rename(src,dst)



'''
remove
删除文件
'''
src = r'C:\Users\Administrator\Desktop\老王.txt'
#src = r'C:\Users\Administrator\Desktop\abcsfsdf'
os.remove(src)