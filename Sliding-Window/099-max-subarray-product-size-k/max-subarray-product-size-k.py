def max_subarray_product_size_k(nums, k):
  curr_prod = 1
  
  for i in range(0, k):
    curr_prod *= nums[i]

  max_prod = curr_prod

  for i in range(0, len(nums) - k):
    curr_prod /= nums[i]
    curr_prod *= nums[i + k]

    max_prod = max(max_prod, curr_prod)
  return max_prod
  
