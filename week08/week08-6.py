class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {} #dict字典
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
        print(d)

        for c in t:
            if c not in d:  #不在字典裡，就是缺他，他就是多出來的
                return c
            if d[c]<= 0 :   #不夠
                return c    #找到多出來的字母
            else:
                d[c]=d[c]-1
        return""