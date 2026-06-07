def find_subarray_sum(nums, target_sum):
  start = 0
  current_sum = 0
  for end in range(0, len(nums)):
    leading_num = nums[end]
    current_sum += leading_num
    while current_sum > target_sum:
      current_sum -= nums[start]
      start+=1
    if current_sum == target_sum:
      return (start, end)
