def has_substring_anagram(s, anagram):
  k = len(anagram)
  window_set = set(s[:k])
  anagram_set = set(anagram)

  if window_set == anagram:
    return True

  for i in range(0, len(s) - k):
    window_set.remove(s[i])
    window_set.add(s[i+k])

    if window_set == anagram_set:
      return True
  return False
