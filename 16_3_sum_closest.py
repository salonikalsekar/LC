class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        ans = dict()   
        nums = sorted(nums)
        
        for i in range(len(nums)):
            left = i+1
            right = len(nums) - 1
            while left < right:
                tempsum = nums[left] + nums[right] + nums[i]
                
                if tempsum == target:
                    return tempsum
                
                elif tempsum < target:
                    left += 1
                else:
                    right -= 1
                    
                ans[tempsum] = abs(target - tempsum)
                
        return min(ans, key=ans.get)
                
            
        
        