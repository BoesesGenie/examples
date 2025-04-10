from random import randrange

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot_index = randrange(len(arr))
        pivot = arr.pop(pivot_index)
        less = [i for i in arr if i <= pivot]
        greater = [i for i in arr if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([9, 1, 5, 2, 4, 3, 6, 8, 7, 0]))
print(quick_sort([0, 9, 1, 5, 2, 4, 5, 3, 6, 7, 8, 7, 0]))
