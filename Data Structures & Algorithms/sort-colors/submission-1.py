class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0 for _ in range(3)]
        for nr in nums:
            freq[nr] += 1
        
        
        counter =0
        for num in range(3):
            for _ in range(freq[num]):
                nums[counter] = num
                counter += 1