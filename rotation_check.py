def is_rotation(word1, word2):
    if len(word1) != len(word2):
        return False

    combined = word1 + word1

    return word2 in combined

print(is_rotation("",""))


