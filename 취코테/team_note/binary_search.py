def binary_search(array, target):
    start, end = 0, len(array) - 1
    while(start<=end):
        mid = (start+end)// 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid - 1
        elif target > array[mid]:
            start = mid + 1
    return -1
            
