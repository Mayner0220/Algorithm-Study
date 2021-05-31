def binary_search(nums: list, target: int) -> int:
    if target not in nums:
        return -1

    left_idx = 0
    right_idx = len(nums)

    while True:
        mid_idx = (left_idx + right_idx) // 2
        mid_value = nums[mid_idx]

        if mid_value == target:
            break
        else:
            if target < mid_value:
                right_idx = mid_idx
            else:
                left_idx = mid_idx

    return mid_idx

nums = [1, 2, 3, 4, 5, 6, 6, 7, 9, 10]
target = 2
print(binary_search(nums, target))