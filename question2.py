def find_disjoint_elements(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    distinct_nums1 = list(set1 - set2)
    distinct_nums2 = list(set2 - set1)

    answer = [distinct_nums1, distinct_nums2]
    return answer
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

answer = find_disjoint_elements(nums1, nums2)
print(answer)  
