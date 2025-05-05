"""  1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity? """

class Solution(object):
     def twoSumSorted(self, nums, target):
        l = 0
        n = len(nums)- 1
        r = n 
        
        while l<r:
            current_sum = nums[l] + nums[r]
            if ( current_sum== target):
                return [l,r]
            elif current_sum < target: 
                l = l+1
            else : 
                r = r - 1 
        return []
    

     def twoSum(self , nums, target):
       seen = {}
       indices = enumerate(nums)
       for i , num in indices : 
           complement = target - num
           if complement in seen : 
              return [seen[complement], i]  
           seen[num] = i 
       return []
           
                
sol = Solution()
nums = [2,7,11,15]
t = 17
print("Final result", sol.twoSum(nums,t))
                
    #def twoSum(self, nums, target):
        

        