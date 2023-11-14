class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary)-max(salary)-min(salary)#全加總-最大-最小
        N = len(salary)-2#全部減兩項(最大 最小)
       
        return total/N