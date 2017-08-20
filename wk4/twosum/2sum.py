from collections import defaultdict

nums = []

with open('2sum.txt') as file:
    for line in file:
        nums.append(int(line))

def binary_search(num, arr):
    if num < arr[0]:
        return 0
    if num > arr[-1]:
        return len(arr) - 1
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low)//2
        if num == arr[mid]:
            return mid
        elif num < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    if arr[low] - num < num - arr[high]:
        return low
    else:
        return high

def two_sum(num_list):

    match = 0

    sorted_list = sorted(num_list)

    # set up dictionary
    num_dict = defaultdict(list)
    for index, num in enumerate(sorted_list):
        num_dict[num].append(index)

    # search
    for t in range(-10000, 10000+1):
        for i in num_dict:
            if t-i in num_dict and t-i >= i:
                match += 1

    return match

print(two_sum(nums))


