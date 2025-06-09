class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n & 1  # Increment count if the last bit is set 
            n >>= 1
        return count    
# Example usage:
solution = Solution()       
print(solution.hammingWeight(11))          # Output: 3
print(solution.hammingWeight(128))         # Output: 1                   