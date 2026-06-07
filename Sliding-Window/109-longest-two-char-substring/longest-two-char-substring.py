from collections import Counter

def longest_two_char_substring(s):
  freq = Counter()
  start = 0
  longest = 0

  for end, leading_char in enumerate(s):
    freq[leading_char] += 1
    
    while len(freq) > 2:
      trailing_char = s[start]
      freq[trailing_char] -= 1
      start += 1
      if freq[trailing_char] == 0:
        del freq[trailing_char]

    if len(freq) == 2:
      longest = max(longest, end-start+1)
  return longest
