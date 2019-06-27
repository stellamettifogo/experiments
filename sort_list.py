
def sort(numbers):
    """ Returns the index of the min and max number. """
    numbers_len = len(numbers)
    # loop esterno (min)
    for i in range(0, numbers_len):
        # loop interno
        for j in range(i +1, numbers_len):
            if numbers[j] < numbers[i]:
                temp = numbers[j]
                numbers[j] = numbers[i]
                numbers[i] = temp
    return numbers

datasets = [
        {
                "series": [7, 9, 3, 5, 2, 0, 8, 1, 4, 6],
                "sorted": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
        },
        {
                "series": [9, 3, 5, 2, 0, 1, 4],
                "sorted": [0, 1, 2, 3, 4, 5, 9] 
        },
        {
                "series": [1, 5, 7, 3, 9],
                "sorted": [1, 3, 5, 7, 9]
        }
]

for data in datasets:
    sorted = sort(data["series"])
    print(sorted)
    assert sorted == data["series"]