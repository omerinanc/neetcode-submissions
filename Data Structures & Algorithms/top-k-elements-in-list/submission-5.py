class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap={}
        res=[]
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        # print(hashmap)

        for j in range(k):
            maxKey = max(hashmap, key=hashmap.get)
            res.append(maxKey)
            del hashmap[maxKey]
            # print(res)
        return res
    