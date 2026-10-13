class Solution:
    def threeSum(self, nums):
        nums.sort()
        triplets = []

        i = 0
        l, r = 1, len(nums) - 1
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                l, r = i + 1, len(nums) - 1
                continue

            if l >= r:
                i += 1
                l, r = i + 1, len(nums) - 1
                continue

            target = nums[i]
            s = -(nums[l] + nums[r])

            if target == s:
                triplets.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif target < s: 
                l += 1
            else:            
                r -= 1
        return triplets





        # if all(x > 0 for x in nums):
        #     return []

        # if all(x < 0 for x in nums):
        #     return []

        # triplets=[]
        # nums.sort()

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             temp = [nums[i],nums[j],nums[k]]
        #             if nums[i] == -(nums[j]+nums[k]):
        #                 if temp not in triplets:
        #                     triplets.append(temp)
        #             elif nums[j] == -(nums[i]+nums[k]):
        #                 if temp not in triplets:
        #                     triplets.append(temp)
        #             elif nums[k] == -(nums[j]+nums[i]):
        #                 if temp not in triplets:
        #                     triplets.append(temp)

        # return triplets