# Define a function that will return the largest number in the list

def max_num(nums):
  default_maximum = nums[0]
  for num in nums:
    if num > default_maximum:
      default_maximum = num
  return default_maximum

print(max_num([50, -10, 0, 75, 20]))