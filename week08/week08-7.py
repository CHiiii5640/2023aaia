class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):#先做兩個字串長度檢查
            return False
        d = {}  #空字典
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
        #print(d)

        for c in t:
            if c not in d: #不在統計的字典裡
                return False
            if d[c] <= 0:
                return False
            else:
                d[c] = d[c] -1

        return True     