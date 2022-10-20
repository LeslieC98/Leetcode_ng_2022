

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)

        if s_count == t_count:
            return True
        if len(s) != len(t):
            return False