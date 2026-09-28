class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1) freq count -> overwrite nums. O(2n)
        count = {0: [], 1: [], 2: []}

        for nr in nums:
            count[nr].append(nr)

        nums[:] = count[0] + count[1] + count[2]
        
