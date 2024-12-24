def first_non_repeating_character(word):
    char_counter = {}
    for char in word:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1    
        
    for char,counter in char_counter.items():
        if counter == 1:
            return char
    
    return None

print(first_non_repeating_character("swiss"))