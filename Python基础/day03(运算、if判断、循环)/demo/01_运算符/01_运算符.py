ret = (True and False)
print(ret)

ret = (True and True)
print(ret)

ret = (False and False)
print(ret)


print('*'*30)

ret = (True or False)
print(ret)

ret = (True or True)
print(ret)

ret = (False or False)
print(ret)

print('*'*30)
ret = not(1>0)
print(ret)

print('*'*30)
ret = False and False or True
print(ret)


print('*'*30)
ret = (True and 110)
print(ret)
ret = (False and 110)
print(ret)
ret = (10 or False )
print(ret)

ret = (None and True )
print(ret)


print('*'*30)

print(0==False)
print(None==False)
print(''==False)
print(1==False)
print(10==True)


#	if条件    0做判断的时候，就是False,非0就是True

print('*'*30)

print('a' in 'abc')
print('a' not in 'abc')

ls1 = [12,3,4,5]
ls2 = [12,3,4,5]
#==判断里面存储的值是否相等
print(ls1==ls2)
#is是用来判断对象的地址是否相等,这里ls1和ls2这两个列表对象，是存储在不同内存空间里，只是里面的值相等罢了。
print(ls1 is ls2)
print(ls1 is not ls2)

'''
	开发中，判断数字和字符串是否相等，使用 ==
'''