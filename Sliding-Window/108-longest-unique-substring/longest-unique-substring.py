from collections import Counter

def longest_unique_substring(s):
  window_counter = Counter()
  longest = 0

  start = 0
  for end in range(len(s)):
    leading_char = s[end]
    window_counter[leading_char] += 1

    while window_counter[leading_char] > 1:
      trailing_counter = s[start]
      window_counter[trailing_counter] -= 1
      start+=1

    longest = max(longest, end - start + 1)
  return longest
