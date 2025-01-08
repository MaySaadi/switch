def anagrams(s1,s2):
    dict = {}

    if len(s1) != len(s2):
        return False
    else:
        for element in s1:
            if element in dict:
                dict[element] +=1
            else:
                dict[element] = 1

        for element in s2:
            if element not in dict:  
                return False          
        return True    
    
print(anagrams("listen","silent"))    
print(anagrams("earth","heart"))    
print(anagrams("aa","bb"))    
print(anagrams("aba","bab"))

# the solution doesn't work for the last example 


def areAnagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    if len(s1) != len(s2):
        return False
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return all(value == 0 for value in char_count.values())


print(areAnagrams("aba","bab")) 
# now works
