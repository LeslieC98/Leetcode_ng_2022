class Soultion:
    def slides(self,s):

        res = 0

        s = [int(c) for c in s]
        print(s)
        n = len(s)

        for i in range(n):
            left = right =i
            while i +1 < n and abs(s[i] - s[i+1]) <= 1:
                i+=1
                right +=1
            res = max(res, right-left +1)
        return res

if __name__ == '__main__':
    s = "1000000"
    print(Soultion().slides(s))

