class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for j in range(len(nums)):
                print(j)
                ans.append(nums[j])
        return ans