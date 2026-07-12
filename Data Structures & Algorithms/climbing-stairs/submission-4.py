class Solution:
    def climbStairs(self, n: int) -> int:
        # 4 icin 1+1+1+1 veya 2 + 1 + 1 veya 2 + 2 veya 1 + 2 + 1 veya 1 + 1 + 2  = 5
        # 5 olsa 1+1+1+1+1 veya 2+2+1 2+1+2 1+2+2 2+1+1+1 1+2+1+1 1+1+2+1 1+1+1+2 = 8
        # 6 olsa 1+1+1+1+1+1 2+1+1+1+1 1+2+1+1+1 1+1+2+1+1 1+1+1+2+1 1+1+1+1+2 2+2+1+1 
        # 2+1+2+1 2+1+1+2 1+2+2+1 1+2+1+2 1+1+2+2 2+2+2 = 13

        if n == 1:
            return 1
        if n == 2:
            return 2

        # return climbStairs(n-1) + climbStairs(n-2)
        a = 1
        b = 2
        total = 0
        while n > 2:
            total = a + b
            a=b
            b=total
            n -= 1
        return total
