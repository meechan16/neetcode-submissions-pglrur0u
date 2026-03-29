class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = {}
        freqi = [[] for i in range(len(nums) + 1)]

        for i in nums:
            dicti[i] = 1+ dicti.get(i, 0)
        
        for num, cnt in dicti.items():
            freqi[cnt].append(num)

        res = []

        for i in range(len(freqi) - 1, 0 , -1):
            for num in freqi[i]:
                res.append(num)
                if len(res) == k:
                    return res