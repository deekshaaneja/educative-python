# Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
import  math

def smallest_subarray_with_given_sum(s, arr):
    windowStart = 0
    minSize = math.inf
    currentSum = 0
    for windowEnd in range(len(arr)):
        if currentSum < s:
            currentSum += arr[windowEnd]
        else:
            currentSum += arr[windowEnd]
            while currentSum - arr[windowStart] >= s:
                currentSum -= arr[windowStart]
                windowStart += 1
                minSize = min(minSize, windowEnd-windowStart+1)
            # currentSum = 0
    return minSize

def main():
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()