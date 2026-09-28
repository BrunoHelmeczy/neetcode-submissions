class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0
        for n in nums:
            res = n if count == 0 else res
            if n == res:
                count += 1
            else:
                count -= 1
        return res
        