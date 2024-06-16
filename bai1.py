def max_in_sliding_window(num_list, k):
    if not num_list or k <= 0:
        return []

    result = []
    for i in range(len(num_list) - k + 1):
        window = num_list[i:i + k]
        max_value = max(window)
        result.append(max_value)
    
    return result

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_in_sliding_window(num_list, k))
