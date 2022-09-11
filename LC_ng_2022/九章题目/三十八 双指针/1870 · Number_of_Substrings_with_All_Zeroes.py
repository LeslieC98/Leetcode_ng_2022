


class Solution:
    """
    @param str: the string
    @return: the number of substrings
    """

    def string_count(self, str: str) -> int:
        # Write your code here.

        if not str:
            return 0

        j, answer = 1, 0

        for i in range(len(str)):
            if str[i] != '0':
                continue
            j = max(j, i + 1)
            while j < len(str) and str[j] == '0':
                j += 1
            # 关键是找到了下标与全零子串个数的关系
            # 子串数目 = 全零子串的长度
            # 比如 000包括了：000，00，0三个子串
            answer += j - i

        return answer


if __name__ == '__main__':
    str1 = "00010011"
    print(Solution().string_count(str1))
