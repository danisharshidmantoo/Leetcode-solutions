class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        l,r = 0,2
        result = 2
        possibleSum = defaultdict(int)
        possibleSum[(nums[0]+nums[1])] += 1
        # possibleSum.add(nums[0]+nums)
        while r<len(nums):
            #calculate all possible sum in subarray[l,r]
            # possibleSum = set()
            for i in range(l,r):
                possibleSum[(nums[i] + nums[r])] += 1
            #check
            count = 0
            for i in range(l,r+1):
                if nums[i] in possibleSum and possibleSum[nums[i]]!= 0:
                    break
                count += 1
            if count != r-l+1:
                 for i in range(l+1,r+1):
                        if (nums[l] + nums[i]) in possibleSum and possibleSum[(nums[l] + nums[i])] != 0:
                            possibleSum[(nums[l]+nums[i])] -= 1
                 l += 1
            if count == r-l+1:
                result = max(result,r-l+1)
            r += 1
        return result
                