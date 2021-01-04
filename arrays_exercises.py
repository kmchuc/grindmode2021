
nums = [10, 20, 30]

def array_max(nums):

    maximum = 0
    for i in nums: #O(n)
        if i > maximum:
            maximum = max(maximum, i) #O(1)
    return maximum

array_max(nums)

#runtime = O(n) worst case scenario
