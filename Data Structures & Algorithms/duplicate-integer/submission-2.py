class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_ = set()

        for nr in nums:
            if nr in set_:
                return True
            
            set_.add(nr)
        return False