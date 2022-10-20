from matplotlib import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dic_s = collections.Counter(s)
        dic_t = collections.Counter(t)
        print(dic_t)
        res = 0
        for c in dic_t: ##打印key,c是否在dict_t的key里

            if c not in dic_s:
                res += dic_t[c]
            else:
                if dic_s[c] > dic_t[c]:
                    n = (dic_s[c] - dic_t[c])
                    res += n
        return res
