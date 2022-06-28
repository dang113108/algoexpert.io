def tournamentWinner(competitions, results):
    source = {}
    for index, sub_array in enumerate(competitions):
        subject = sub_array[results[index] ^ 1]
        if subject not in source:
            source[subject] = 3
        else:
            source[subject] += 3

    return max(source, key=lambda k: source[k])
