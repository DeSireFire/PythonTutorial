def erfen(list,item):

	first = 0
	last = len(list)-1

	while first<=last:
		
		mid = (first + last)//2
		if list[mid] == item:
			return True
		elif list[mid] > item:
			last = mid - 1
		else:
			first = mid + 1
	return False

if __name__ == '__main__':
	list = [44,55,2,14,36,65,25]
	print(erfen(list,360))
