class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        tmp, tmp2, result = 0, 0, 0
        if len(stones) == 1:
            return stones[0]
            
        for i in range(len(stones)-1):
            tmp = max(stones)
            stones.remove(tmp)
            tmp2 = max(stones)
            stones.remove(tmp2)
            result = tmp - tmp2
            stones.append(result)
        return result
