# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

import math

def find_averages_of_subarrays(K, arr):
    window_start = 0
    current_sum = 0
    res = []

    for window_end in range(len(arr)):
        if window_end < K:
            current_sum += arr[window_end]
        else:
            res.append(current_sum)
            current_sum = current_sum - arr[window_start] + arr[window_end]
            window_start += 1
    res.append(current_sum)
    return res

def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()


