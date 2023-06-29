def reorganize_array(nums, n):
    first_half = nums[:n]
    second_half = nums[n:]

    result = []

    for i in range(n):
        result.append(first_half[i])
        result.append(second_half[i])

    return result
nums = [2, 5, 1, 3, 4, 7]
n = 3

reorganized_nums = reorganize_array(nums, n)
print(reorganized_nums)  
