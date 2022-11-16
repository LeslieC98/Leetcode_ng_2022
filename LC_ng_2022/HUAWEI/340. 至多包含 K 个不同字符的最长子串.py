import collections


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if len(s) == 0 or k == 0:
            return 0
        ls = len(s)
        left = right = 0
        dic = collections.defaultdict()
        max_len = 1
        while right < ls:
            # 右指针移动前进一步，写入字典（指针的那个字符的index）
            dic[s[right]] = right
            right += 1
            # 当右指针写入字典后，字典长度为k+1的时候，找到左指针指向的字符的index，
            # 把他除去出字典，同时，移动左指针前进一步
            if len(dic) == k + 1:
                # 找最小值的时间复杂度为O(k) n个变量进行1此操作，所以有O（n）时间复杂度 总的时间复杂度为O（NK）
                index_left = min(dic.values())
                del dic[s[index_left]]
                left = index_left + 1

            max_len = max(max_len, right - left) # 步进长度！
        return max_len

if __name__ == '__main__':
    s = "eceba"
    k = 2
    print(Solution().lengthOfLongestSubstringKDistinct(s,k))