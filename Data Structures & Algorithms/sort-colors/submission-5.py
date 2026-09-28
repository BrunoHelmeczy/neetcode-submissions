class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1) freq count -> overwrite nums. O(2n)
        count = {0: 0, 1: 0, 2: 0}
        # count = {0: [], 1: [], 2: []}

        for nr in nums:
            count[nr] += 1
            # count[nr].append(nr)

        nums[:] = [0] * count[0] + [1] * count[1] + [2] * count[2]
        
