def is_rotation(word1, word2):
    if len(word1) != len(word2):
        return False

    combined = word1 + word1

    return word2 in combined

print(is_rotation("",""))


def is_rotation_shift(word1, word2):
    if len(word1) != len(word2):
        return False

    rotated = word1
    for _ in range(len(word1)):
        rotated = rotated[1:] + rotated[0]  
        if rotated == word2:
            return True

    return False
