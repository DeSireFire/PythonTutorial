ls = [23,100,88,10,7]

def bubbling_sort(nums):
    n = len(nums)
    for i in range(1,n):
          for j  in range(0,n-i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]

bubbling_sort(ls)
print(ls)