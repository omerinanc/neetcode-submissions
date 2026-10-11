class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1 and nums[0] != 0:
            return 0

        for i in range(len(nums)-1):
            if i == 0 and nums[i] != 0:
                return 0
        
            if (nums[i] + 1) != nums[i+1]:
                return nums[i]+1
        nums = nums[::-1]
        return nums[0]+1
        