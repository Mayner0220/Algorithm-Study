# https://www.acmicpc.net/problem/11057

N = int(input())
nums = [1] * 10

for _ in range(N-1):
    for i in range(1, 10):
        nums[i] = (nums[i] + nums[i-1]) % 10007

print(sum(nums) % 10007)