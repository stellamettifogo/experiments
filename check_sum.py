
#devi fare pratica!!!

def check_sum(values: [int], sum: int) -> bool:
    values_len = len(values)

    for i in range(0, values_len -1):
        for j in range(i +1, values_len):
            if values[i] + values[j] == sum:
                return True

    return False


dataset = [9, 12, 5, 3, 6, 18, 7, 12]
assert check_sum(dataset, 17)

dataset = [9, 12, 5, 3, 6, 18, 7, 12]
assert check_sum(dataset, 18)

dataset = [9, 12, 5, 3, 6, 18, 7, 12]
assert check_sum(dataset, 27)

dataset = [9, 12, 5, 3, 6, 18, 7, 12]
assert check_sum(dataset, 2000) == False
#oppure
assert not check_sum(dataset, 2)


