# Find the common elements between 2 arrays.
#Brute force solution in o(n^2)
def find_common_in_2_arrs_brutef(arr1,arr2):
    common = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                common.append(arr1[i])
    return common

def find_common_in_2_arrs(arr1,arr2):
    dicti = {}
    for element1 in arr1:
        if element1 not in dicti:
            dicti[element1] = False
                
                

    for element2 in arr2:
        if element2 in dicti:
            dicti[element2] = True  

    common = []
    for key, value in dicti.items():
        if value == True:
            common.append(key)
    return common      

    



# Find the common elements among three arrays
def find_common_in_3_arrs(arr1,arr2,arr3):  
    dicti = {}
    for element1 in arr1:
        if element1 not in dicti:
            dicti[element1] = False
                
                

    for element2 in arr2:
        if element2 in dicti:
            dicti[element2] = True  

    common = []
    for key, value in dicti.items():
        if value == True:
            common.append(key)
            
    for element3 in dicti:
        if element3 not in arr3:
            common.remove(element3)
    return common      

    
arr1 = [1,3,5,2]
arr2 = [2,3,4,5,1]
arr3 = [2,3,4]

print(find_common_in_2_arrs_brutef(arr1,arr2))
print(find_common_in_2_arrs(arr1,arr2))

print(find_common_in_3_arrs(arr1,arr2,arr3))
    

    

#warmup
# number of vowels:
def count_vowels(txt):
    counter = 0
    for _ in txt:
        if _ in "aeouiAEOUI" :
            counter += 1
    return counter        

txt = "Maymmaaahus"
print("Number of vowels is:",count_vowels(txt))
print("Number of consonants is:", len(txt) - count_vowels(txt)  )

#biggest number in 3 words:
def find_biggest(num1,num2,num3):
    if (num1>num2 and num1>num3):
        return num1
    elif num2 >num1 and num2>num3 :
        return num2
    else: 
        return num3

print("The biggest number is:",find_biggest(5,5,7))

#Median char
def find_median_char_manual(string):
    characters = list(string)
    for i in range(len(characters)):
        min_index = i
        for j in range(i + 1, len(characters)):
            if characters[j] < characters[min_index]:
                min_index = j
        characters[i], characters[min_index] = characters[min_index], characters[i]

    length = len(characters)
    if length % 2 == 1: 
        median_char = characters[length // 2]
    else:  
        median_char = characters[length // 2 - 1]  
    return  median_char



def get_highest_scoring_word(input_string):
    words = input_string.split()
    def word_score(word):
        return sum(ord(char) - ord('a') + 1 for char in word)
    
    max_score = 0
    best_word = ""
    
    for word in words:
        score = word_score(word)
        if score > max_score:
            max_score = score
            best_word = word
    
    return best_word
