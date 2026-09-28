class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, nr in enumerate(nums):
            if target - nr in mp.keys():
                return [mp[target - nr], i]
            else:
                mp[nr] = i

        