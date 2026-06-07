def longest_subarray_sum(nums, target_sum):
  start = 0
  window_sum = 0
  max_length = -1
  
  for end in range(len(nums)):
    leading_num = nums[end]
    window_sum += leading_num
    while window_sum > target_sum:
      window_sum -= nums[start]
      start += 1
    if window_sum == target_sum:
      max_length = max(max_length, end - start + 1)
  return max_length
