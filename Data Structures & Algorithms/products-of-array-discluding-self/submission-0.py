class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, i, j =[], 0, 0

        for i in range(len(nums)):
            temp, x = [], 1
            for j in range(len(nums)):
                if i == j:
                    continue
                temp.append(nums[j])
            for val in temp:
                x = x * val
            res.append(x)
        return res
