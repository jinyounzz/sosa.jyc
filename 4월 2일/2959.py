#2959
nums = list(map(int, input().split()))
nums.sort()
area = nums[0] * nums[2]
print(area)