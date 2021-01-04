
nums_1 = [2, 4, 6, 8, 10]
nums_2 = [4, 6, 8, 10, 12]

def common_num(nums1, nums2):

    common = []

    for i in nums_1:
        for j in nums_2:
            i_current = 0
            j_current = 0

            if nums_1[i_current] == nums_2[j_current]:
                common.append(nums_1[i])
                i_current += 1
            else:
                j_current += 1
                continue
    print(common)
    return common

common_num(nums_1, nums_2)