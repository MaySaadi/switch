def second_max(arr):
    max1 = arr[0]
    for number in arr[1:]:
        if number> max1:
            max1 = number


    max2 = arr[0]
    for element in arr[1:]:
        
        if max2 < element and element != max1:
            max2 = element

    return max2

         

print(second_max([1,5,6,7,8,-5,-100]))        