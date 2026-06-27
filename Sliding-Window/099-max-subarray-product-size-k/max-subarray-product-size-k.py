def max_subarray_product_size_k(nums, k):
  current_product = 1
  for i in range(0, k):
    current_product *= nums[i]
  max_product = current_product

  for i in range(0, len(nums)-k):
    
