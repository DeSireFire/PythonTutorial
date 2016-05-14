#斐波那契数列
def c(m):
	if m == 1 or m == 2:
		return 1
	return c(m-1)+c(m-2)

print(c(10))

