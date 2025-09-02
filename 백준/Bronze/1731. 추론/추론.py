import sys

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]

common_difference = nums[1] - nums[0]
is_arithmetic = True

for i in range(2, n):
  if nums[i] - nums[i-1] != common_difference:
    is_arithmetic = False
    break

if is_arithmetic:
  print(nums[-1] + common_difference)
else:
  common_ratio = nums[1] // nums[0]
  print(nums[-1] * common_ratio)