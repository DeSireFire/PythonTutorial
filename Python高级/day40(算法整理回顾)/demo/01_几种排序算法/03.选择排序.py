def selection_sort(list2):
	for i in range(0, len (list2)):
		min = i
		for j in range(i + 1,len(list2)):
			if list2[j] < list2[min]:
				min = j
		list2[i], list2[min] = list2[min], list2[i]

if __name__ == '__main__':

    ls = [11,22,88,66,77,99,44,55,33]
    selection_sort(ls)
    print(ls)
