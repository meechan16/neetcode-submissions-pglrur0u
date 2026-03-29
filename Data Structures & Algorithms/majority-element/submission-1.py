class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # moore's voting lmfao
        cnt = 1
        ini = nums[0]
        for i in nums[1:]:
            if i == ini:
                cnt+=1
            else:
                if cnt == 0:
                    ini =i
                    cnt+=1
                else:
                    cnt-=1
        return ini
                