class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        res = 0

        for i in arr:
            if i-1 not in arr:
                l = 1
                while(i+l) in arr:
                    l+=1
                res = max(l, res)

        return res