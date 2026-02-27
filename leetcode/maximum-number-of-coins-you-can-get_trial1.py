class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        n = len(piles)
        left = 0
        right = n - 1
        
        result = 0
        
        while left < right:
            # Alice takes largest
            right -= 1
            
            # You take second largest
            result += piles[right]
            right -= 1
            
            # Bob takes smallest
            left += 1
        
        return result