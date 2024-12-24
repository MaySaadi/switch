def find_colsest_number(arr,num):
    dict = {}
    for element in arr:
        if element in dict:
            continue
        else:
            diff = element - num
            if diff < 0 :
                diff = diff * -1
                dict[element] = diff

            elif diff == 0:
                return element
            else:
                dict[element] = diff
    closest_number = dict[arr[0]]

    for element in arr[1:]:
        if dict[element] < closest_number :
            closest_number = element
    return closest_number

print(find_colsest_number([1,2,5,4,3,9,0],-5))