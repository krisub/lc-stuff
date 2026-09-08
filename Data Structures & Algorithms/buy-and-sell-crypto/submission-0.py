class Solution:
    '''
    [10,1,5,6,7,1]

    [7,1,5,3,6,4]
    

    '''
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        min_so_far = prices[0]

        for i in range(1, len(prices), 1):
            max_profit = max(max_profit, prices[i] - min_so_far)
            min_so_far = min(min_so_far, prices[i])

        return max_profit