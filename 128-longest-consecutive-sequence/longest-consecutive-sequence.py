class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        st = set(nums)

        result = 0
        for n in st:
            if n-1 not in st:
                count = 1
                while n+1 in st:
                    count += 1
                    n += 1
                result = max(result,count)
        return result
