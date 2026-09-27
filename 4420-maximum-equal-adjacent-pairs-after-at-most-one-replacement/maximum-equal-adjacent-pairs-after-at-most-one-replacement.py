class Solution:

    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:

        init = 0

        count = defaultdict(int)

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                init += 1
                count[nums[i]] += 1

        adjcount = defaultdict(int)

        for i in range(len(nums)-1):
            adjcount[(nums[i], nums[i+1])] += 1

        result = init

        for a, b in adjcount:

            if a == b:
                continue

            pairs = adjcount.get((a,b), 0) + adjcount.get((b,a), 0)

            result = max(result, init + pairs)

        return result