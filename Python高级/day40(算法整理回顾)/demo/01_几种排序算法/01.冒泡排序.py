def Mybubbing(num):
	n = len(num)
	for i in range(1,n):
	 	for j in range(0,n-i):
	 		if num[j] > num[j+1]:
	 			num[j],num[j+1]=num[j+1],num[j]
	print(num)
	print(lala)
	
# 最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
# 最坏时间复杂度：O(n2)
# 稳定性：稳定
if __name__ == "__main__":

	lala=[55,7,23,89,45,110,95]
	Mybubbing(lala)
	
