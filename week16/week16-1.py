class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s)
        ans=0
        for left in range(N-1):
            #測試左邊幾個0，右邊幾個1
            now = 0 #現在的值是多少
            for i in range(N): #每個字母檢查
                if i <= left and s[i]=="0": now += 1
                if i > left and s[i] == "1": now += 1
            if now > ans: ans=now #更新答案
        return ans