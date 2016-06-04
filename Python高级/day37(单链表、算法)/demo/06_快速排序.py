def quick_sort(nums,start,end):

    if start >= end:
        return


    mid = nums[start]
    low = start
    high = end


    while low<high:
        while low<high and nums[high]>=mid:
            high-=1
        nums[low] = nums[high]

        while low<high and nums[low]<mid:
            low+=1
        nums[high] = nums[low]

    nums[low] = mid

    quick_sort(nums,start,low-1)
    quick_sort(nums, low+1, end)

if __name__ == '__main__':
    alist = [11,2,11]
    quick_sort(alist,0,len(alist)-1)
    print(alist)
