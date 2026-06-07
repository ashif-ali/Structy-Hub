from collections import Counter

def count_substring_anagrams(s, anagram):
  k = len(anagram)
  anagram_freq = Counter(anagram)
  window_freq = Counter(s[:k])

  count = 0
  if anagram_freq == window_freq:
    count += 1

  for i in range(0, len(s) - k):
    left = s[i]
    right = s[i + k]

    window_freq[left] -= 1
    if window_freq[left] == 0:
      del window_freq[left]

    window_freq[right] += 1

    if window_freq == anagram_freq:
      count += 1
  return count
