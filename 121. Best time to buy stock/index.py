class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        maxProfit = 0
        cheapest = prices[0]
        for i in prices:
            if i - cheapest > 0:
                if maxProfit < (i - cheapest):
                    maxProfit = i - cheapest
            if i < cheapest:
                cheapest = i

        return maxProfit


"""
Based on the fact that we have to sell after we buy and we are trying to maximize profit, we can iterate through the prices and only need to consider two things:
1.) Is this price cheaper than any other price I've seen before?
2.) If I subtract current price by the cheapest price I've found, does this yield a greater profit than what I've seen so far?

A fun thing to note is if #1 is true, then #2 cannot be true as well so there isn't a need to check

Let's consider an example of [4,1,5,2,7]

4 is the cheapest price we see to start, and we can't sell on the first day so maxProfit is 0
1 is now the cheapest price we've seen. Selling now would lose us money, so we can't update maxProfit
5 is not cheaper than 1, but if we sell now we get a maxProfit of 4! Better save that for later
2 is not cheaper than 1 and if we sell, we only get a profit of 1, no need to do anything here
7 is not cheaper than 1, but if we sell here, we'll increase maxProfit to 6, making this the best profit to return.
Hope this helps someone else!
"""
