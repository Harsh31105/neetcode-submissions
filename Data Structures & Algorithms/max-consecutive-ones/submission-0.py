class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        streak = 0
        for i, num in enumerate(nums):
            if num == 1:
                streak = streak + 1   
                if i == len(nums) - 1:
                    max_streak = max(max_streak, streak)      
            else:
                max_streak = max(max_streak, streak)
                streak = 0
        
        return max_streak