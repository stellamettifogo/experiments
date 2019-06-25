

def palindrome(word):
    """ Returns the index of the word """
    word_len = len(word)
    max_pal_index = 0
    max_pal_size = 0
    # loop esterno (index)
    for i in range(0, word_len - 1):
        # loop interno (size)
        pal_size = 1
        while pal_size <= min(i +1, word_len -i -1) and word[i - pal_size +1] == word[i + pal_size]:
            if pal_size > max_pal_size:
                max_pal_size = pal_size
                max_pal_index = i
            pal_size = pal_size + 1

    if max_pal_size < 1:
        return None
    return word[max_pal_index - max_pal_size +1: max_pal_index + max_pal_size +1]



datasets = [
    [ "anna", "anna"],
    [ "melone", None],
    ["banana", None],
    ["bananna", "anna"],
    ["aaaabcdeedcbarrrr", "abcdeedcba"]
]

for data in datasets:
    pali = palindrome(data[0])
    assert pali == data[1]

