from collections import Counter

def almostAnagrams(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    count1 = Counter(s1)
    count2 = Counter(s2)

    diff = sum((count1 - count2).values()) + sum((count2 - count1).values())

    if diff == 1:
        return "1 missing letter"
    elif diff == 2:
        return "1 replacement"
    else:
        return "Not almost anagrams"

print(almostAnagrams("abc", "ba"))       # Output: "1 missing letter"
print(almostAnagrams("abc", "cna"))      # Output: "1 replacement"
print(almostAnagrams("hello", "world"))  # Output: "Not almost anagrams"