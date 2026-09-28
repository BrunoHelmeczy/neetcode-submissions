class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # split
        def split(nums):
            mid = len(nums) // 2
            return [nums[:mid], nums[mid:]]
        # sort
        def sort(nums):
            if len(nums) ==1:
                return nums
            left, right = split(nums)
            left = sort(left)
            right = sort(right)
            return merge(left, right)
        def merge(left, right):
            result = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i +=1
                else:
                    result.append(right[j])
                    j +=1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        return sort(nums)
            
