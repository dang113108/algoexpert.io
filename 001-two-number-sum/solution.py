def twoNumberSum(array, targetSum):
    array_len = len(array)
    for i in range(array_len - 1):
        first_int = array[i]
        for j in range(i + 1, array_len):
            second_int = array[j]
            if first_int + second_int == targetSum:
                return [first_int, second_int]
    return []
