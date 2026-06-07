def has_substring_anagram(s, anagram):
  k = len(anagram)
  window_set = set(s[:k])
  anagram_set = set(anagram)
  if window_set == anagram_set:
    return True

  for i in range(0, len(s) - k):
    window_set.remove(s[i])
    window_set.add(s[i+k])
    if anagram_set == window_set:
      return True
  return False
    
