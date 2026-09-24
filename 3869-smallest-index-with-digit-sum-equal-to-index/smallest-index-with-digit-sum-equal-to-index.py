class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def calc(n):
            result = 0
            while n:
                result += n % 10
                n //=10
            return result
        for i,n in enumerate(nums):
            if calc(n) == i:
                return i
        return -1