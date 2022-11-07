#* 用一个栈模拟，栈中元素为一个 tuple (letter, count)，第一个值为字母，第二个为它的连续重复次数；
##use a stack to simulate the process and the element in stack is a tuple[letter,count]
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        ## s = "deeedbbcccbdaa", k = 3
        stack = []  ##[char,count] 或者stack[0,0]   存储成 d:2, e:3, a:2...
        for i in s:  ##e:1
            if stack and stack[-1][0] == i:  ##stack exist and the top of stack is equal to i; e在前面有了
                stack[-1][-1] += 1  ## [[d,1],[e:1]] => [[d,1],[e:2]]
            else:  ##not euqal
                stack.append([i, 1])

            if stack[-1][-1] == k:
                stack.pop()

        ans = ""
        ##stack = [['a', 2]]
        for char, count in stack:
            ans += (char * count)

        return ans

##time:O(n) space O(n)