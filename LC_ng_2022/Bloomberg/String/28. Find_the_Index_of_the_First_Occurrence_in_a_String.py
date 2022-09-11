"""
1. brute force
时间复杂度：0（nxm），其中n 是字符串haystack 的长度，m是宇符串needle 的长度。最坏情况下
我们需要将字符串 needle 与字符串 haystack 的所有长度为 m 的子串均匹配一次
空间复杂度：0(1)。我们只需要常数的空间保存若干变量。
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        for i in range(m):
            if haystack[i:i+n] == needle:
                return i
        return -1

