class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashmap = {}

        for word in strs:
            string = "".join(sorted(word))
            if string in hashmap:
                ans[hashmap[string]].append(word)
            else:
                hashmap[string] = len(ans)
                ans.append([word])
        return ans