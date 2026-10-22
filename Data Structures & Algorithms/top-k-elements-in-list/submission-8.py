class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap= {}
        res = []

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1 
            else:
                hashmap[nums[i]] = 1

        j = 0
        while j < k:
            maxKey = max(hashmap, key=hashmap.get)
            res.append(maxKey)
            del hashmap[maxKey]
            j +=1
        return res
