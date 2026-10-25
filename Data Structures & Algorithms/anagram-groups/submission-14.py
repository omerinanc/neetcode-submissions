class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        hashmap={}

        for i in strs:
            sortedString = "".join(sorted(i))
            if sortedString in hashmap:
                ans[hashmap[sortedString]].append(i)
            else:
                hashmap[sortedString] = len(ans)
                ans.append([i])
        return ans
            