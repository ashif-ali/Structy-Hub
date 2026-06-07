def subarray_target_sum_size_k(nums, target, k):
  window_sum = 0
  for i in range(0, k):
    window_sum += nums[i]

  count = 1 if window_sum == target else 0



  for i in range(0, len(nums) - k):
    window_sum += nums[i + k]
    window_sum -= nums[i]
    if window_sum == target:
      count+=1
  return count
