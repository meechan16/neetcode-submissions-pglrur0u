class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumi = 0
        res = nums[0]
        for i in nums:
            if sumi<0:
                sumi = 0
            sumi +=i
            res = max(res, sumi)
        return res