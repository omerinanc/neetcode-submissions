class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberFreq = {}
        i = 0
        while i < len(nums):
            if nums[i] not in numberFreq:
                count = 0
                j = i
                while j < len(nums):
                    if nums[j] == nums[i]:
                        count += 1
                    j += 1
                numberFreq[nums[i]] = count
            i += 1

        sorted_nums = sorted(numberFreq, key=lambda x: numberFreq[x], reverse=True)
        return sorted_nums[:k]