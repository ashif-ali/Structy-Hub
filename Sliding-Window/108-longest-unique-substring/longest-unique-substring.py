from collections import Counter

def longest_unique_substring(s):
  start = 0
  longest = 0
  freq = Counter()

  for index, leading_char in enumerate(s):
    freq[leading_char] += 1

    while freq[leading_char] > 1:
      trailing_char = s[start]
      freq[trailing_char] -= 1
      start += 1

    
    
  
