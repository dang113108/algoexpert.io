def isValidSubsequence(array, sequence):
    compare_index = -1
    for num in sequence:
        if num not in array[compare_index + 1:]: return False
        current_index = array[compare_index + 1:].index(num) + compare_index + 1
        if current_index < compare_index:
            return False
        else:
            compare_index = current_index
    return True
