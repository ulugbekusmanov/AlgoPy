def binary_search(arr, search, start, stop):
    if start > stop:
        return False
    else:
        middle = (start + stop) // 2
        print("{} {} {} ".format(middle, start, stop))
        if search == arr[middle]:
            return middle
        elif search < arr[middle]:
            return binary_search(arr, search, start, middle - 1)
        else:
            return binary_search(arr, search, middle + 1, stop)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
start = 0
stop = len(arr)
search = 18
x = binary_search(arr, search, start, stop)
if x == False:
    print("Not found")
else:
    print("Item ", search, "Found at Index ", x)
