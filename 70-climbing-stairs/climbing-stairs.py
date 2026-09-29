class Solution:
    def climbStairs(self, n: int) -> int:
        prev2,prev1 = 1,1
        for n in range(2,n+1):
            temp = prev2 + prev1
            prev2 = prev1
            prev1 = temp
        return prev1