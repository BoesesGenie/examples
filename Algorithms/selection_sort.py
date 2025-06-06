def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selection_sort(arr):
    result = []

    while len(arr):
        index = find_smallest(arr)
        result.append(arr.pop(index))

    return result

print(selection_sort([9, 1, 5, 2, 4, 3, 6, 8, 7, 0]))
