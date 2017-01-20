def insertionSort(nums):
    for i in range(0,len(nums)):
        key = nums[i]
        j = i
        while j > 0 and nums[j-1] > key:
            nums[j] = nums[j-1]
            j = j-1
        nums[j] = key
    return nums
