class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0 #迴圈前面 ans =0

        while n>0: #要把n剝光
            ans += n%2 #剝下來
            n = n // 2 #剝完就變小

        return ans #迴圈後面ans拿來用