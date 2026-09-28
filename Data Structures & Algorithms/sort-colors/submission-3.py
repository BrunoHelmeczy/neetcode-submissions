class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1) freq count -> overwrite nums. O(2n)
        count = {}

        for nr in nums:
            if nr not in count.keys():
                count[nr] = [nr]
            else:
                count[nr].append(nr)

        nums[:] = count.get(0, []) + count.get(1, []) + count.get(2, [])
        