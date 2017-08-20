nums = []


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

with open('2sum.txt') as file:
    for line in file:
        nums.append(int(line))

sorted_nums = sorted(nums)

def two_sum(num_list):

    match = 0

    sorted_list = sorted(num_list)

    # locate admissible range for y
    for num in sorted_list:
        t_l = -10000 - num
        t_h = 10000 - num

        num_list_l = binary_search(t_l, sorted_list)
        num_list_h = binary_search(t_h, sorted_list)

        


