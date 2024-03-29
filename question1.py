def find_common_elements(arr1, arr2, arr3):
    ptr1 = ptr2 = ptr3 = 0
    result = []

    while ptr1 < len(arr1) and ptr2 < len(arr2) and ptr3 < len(arr3):
        if arr1[ptr1] == arr2[ptr2] == arr3[ptr3]:
            result.append(arr1[ptr1])
            ptr1 += 1
            ptr2 += 1
            ptr3 += 1
        elif arr1[ptr1] < arr2[ptr2]:
            ptr1 += 1
        elif arr2[ptr2] < arr3[ptr3]:
            ptr2 += 1
        else:
            ptr3 += 1

    return result
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]

result = find_common_elements(arr1, arr2, arr3)
print(result)
