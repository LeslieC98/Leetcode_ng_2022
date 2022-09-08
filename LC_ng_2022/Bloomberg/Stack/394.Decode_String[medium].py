class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_num = ''
        cur_str = ''

        for char in s:  # 字符串 CHAR
            if char == '[':
                stack.append(cur_str)
                stack.append(int(cur_num)) ##转为数字
                cur_num = ''
                cur_str = ''
            elif char ==']':
                num = stack.pop()
                prev_str = stack.pop()
                cur_str = prev_str + cur_str * num
            elif char.isdigit():
                cur_num += char
            else:
                cur_str += char
        return cur_str
