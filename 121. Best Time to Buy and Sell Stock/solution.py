# loop throught the list in reversed order and keep track of max price and max profir possible

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = -1
        max_prof = -1
        for price in reversed(prices):
            if price >= max_val:
                max_val = price 
            if max_prof < max_val - price:
                max_prof = max_val - price
        return max(0, max_prof) 

