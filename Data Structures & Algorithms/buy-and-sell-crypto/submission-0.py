class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minAmount = float('inf')
        maxProfit = 0
        for p in prices:
            minAmount = min(minAmount, p)
            maxProfit = max(maxProfit, p - minAmount)
        return maxProfit
    
    '''
    [10,1,5,6,7,1]
    [10,8,7,5,2]
    p = 8
    minAmount = 8
    maxProfit = 0
    '''
