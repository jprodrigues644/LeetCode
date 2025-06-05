class Solution(object):
    def containsDuplicate(self, nums):
         return len(nums) != len(set(nums))
    #    """  # nums.sort()
        
    #    """  for i in range (len(nums) - 1) :
    #         if nums[i]==nums[i+1] :
    #             return True
    #     return False """ """
           
    
if __name__ == "__main__":
    nums = [1 , 2 , 3 ]
    sol = Solution()
    print(sol.containsDuplicate(nums))  
            
            
    