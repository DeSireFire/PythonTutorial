"""
适用于有序的列表
"""

def binary_search(lists,item):
    first = 0
    end = len(lists)-1


    while first<=end:
        mid = (first + end) // 2
        if lists[mid]==item:
            return True
        elif lists[mid]<item:
            first = mid+1
        else:
            end = mid-1
    return False


if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(binary_search(testlist,13))

