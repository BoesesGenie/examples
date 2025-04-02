def binary_search(input_list, target):
    low = 0
    high = len(input_list) - 1

    while low <= high:
        mid = (low + high) // 2

        if input_list[mid] < target:
            low = mid + 1
        elif input_list[mid] > target:
            high = mid - 1
        elif input_list[mid] == target:
            return mid

    return -1
