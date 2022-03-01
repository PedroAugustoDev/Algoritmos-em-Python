# function to get min value of array
def get_min(array):
    var1 = 0
    for i in range(0, len(array)):
        if i == 0: var1 = array[i]
        else:
            if array[i] <= var1:
                var1 = array[i]
    return var1


list_num = [23, 44, 55, 9, 235, -1, 90, 1, 3, 4, 5, 6]


# Return -1, because its the smallest value in the list
print(f'The min value of array is: {get_min(list_num)}')