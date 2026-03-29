class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ini = 0
        for i in nums:
            if i != val:
                nums[ini] = i
                ini+=1
        return ini
            