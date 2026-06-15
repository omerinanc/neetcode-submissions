class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keyValues = {}
        used = [False] * len(nums)
        for i in range(len(nums)):
            counter = 1
            if used[i]:
                continue
            used[i] = True
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    used[j]= True
                    counter += 1
            keyValues[nums[i]] = counter
        sorted_items = sorted(keyValues.items(), key=lambda x: x[1], reverse=True)
        result = [item[0] for item in sorted_items[:k]]
        return result