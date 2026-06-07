# def max_subarray_sum_size_k(nums, k):
#   max_sum = float('-inf')
#   for i in range(0, len(nums) - k + 1):
#     current_sum = 0
#     for j in range(i, i + k):
#       current_sum += nums[j]
#     if current_sum > max_sum:
#       max_sum = current_sum
#   return max_sum

  
def max_subarray_sum_size_k(nums, k):
  current_sum = 0
  for i in range(0, k):
    current_sum += nums[i]
  max_sum = current_sum

  for i in range(0, len(nums) - k):
    current_sum -= nums[i]
    current_sum += nums[i+k]
    if current_sum > max_sum:
      max_sum = current_sum
  return max_sum