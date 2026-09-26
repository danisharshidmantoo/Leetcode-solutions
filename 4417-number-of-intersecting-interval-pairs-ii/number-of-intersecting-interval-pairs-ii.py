class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        start = []
        end = []

        for i in range(len(intervals)):
            s,e = intervals[i]
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()
        n = len(intervals)
        total = n*(n-1)//2

        i,j =0,0
        while i<n:

            while end[j]<start[i]:
                j += 1
            total -= j
            i += 1
        return total
