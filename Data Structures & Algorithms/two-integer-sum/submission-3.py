class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i, nr in enumerate(nums):
            needed = target - nr

            if needed in count.keys():
                return [count[needed], i]
            
            count[nr] = i

        return False