def couting_sort(nums, max_num):
    sort_list = [0] * len(nums)
    cnt_list = [0] * (max_num + 1)

    for i in range(len(nums)):
        cnt_list[nums[i]] += 1

    for i in range(1, len(cnt_list)):
        cnt_list[i] += cnt_list[i - 1]

    for i in range(len(nums)):
        sort_list[cnt_list[nums[i]] - 1] = nums[i]
        cnt_list[nums[i]] -= 1

    return sort_list


numbers = [1, 0, 3, 1, 0, 2, 5, 2, 1, 4]
result = couting_sort(numbers, max(numbers))
print(result)