class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()

        for nr in nums:
            if nr in hset:
                return True
            else:
                hset.add(nr)
        return False
        