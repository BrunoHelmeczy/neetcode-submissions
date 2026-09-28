class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def split(nums):
            mid = len(nums) // 2
            return [nums[:mid], nums[mid:]]
        
        def sort(nums):
            if len(nums)==1:
                return nums
            L, R = split(nums)
            L = sort(L)
            R = sort(R)

            return merge(L, R)

        def merge(nums1, nums2):
            i = j = 0
            res = []
            while i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    res.append(nums1[i])
                    i+=1
                else:
                    res.append(nums2[j])
                    j+=1
            res.extend(nums1[i:])
            res.extend(nums2[j:])
            return res
        return sort(nums)
        