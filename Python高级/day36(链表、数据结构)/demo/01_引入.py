import time

start_time = time.time()

# 注意是三重循环
for a in range(0, 1001):
    for b in range(0, 1001):
        for c in range(0, 1001):
            if a**2 + b**2 == c**2 and a+b+c == 1000:
                print("a, b, c: %d, %d, %d" %,  (a, b,c))

end_time = time.time()
print("elapsed: %f" % (end_time - start_time))
print("complete!")


#1000*1000*1000*2
#2*n**3
#3*n**3+10--->3*n**3--->n**3
# if xx:
#     1
#     2
#     3
#     4
# else:
#     1
#     2