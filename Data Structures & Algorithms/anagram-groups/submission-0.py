class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = []
        used = [False] * len(strs) 
        
        for i in range(len(strs)):
            if used[i]:
                continue
            current_group = [strs[i]]
            used[i] = True
            for j in range(i + 1, len(strs)):
                if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                    current_group.append(strs[j])
                    used[j] = True
            grouped.append(current_group)
        
        return grouped
