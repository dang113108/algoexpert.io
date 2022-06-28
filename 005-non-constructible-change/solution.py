def nonConstructibleChange(coins):
    coins.sort()

    current_sum = 0
    for num in coins:
        if num > current_sum + 1:
            break

        current_sum += num

    return current_sum + 1
