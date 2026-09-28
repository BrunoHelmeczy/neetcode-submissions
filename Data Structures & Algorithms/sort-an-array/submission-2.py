class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 1) mergeSort: O(n log n) guaranteed: split, sort each side, merge together
        def split(nums: list[int]) -> list[list[int]]:
            mid = len(nums) // 2
            return [nums[:mid], nums[mid:]]

        def sort(nums: list[int]) -> list[int]:
            if len(nums) == 1:
                return nums

            left, right = split(nums)

            left = sort(left)
            right = sort(right)

            result = merge(left, right)
            return result

        def merge(left: list[int], right: list[int]) -> list[int]:
            i, j, = 0, 0
            result = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        return sort(nums)

        # 2) quickSort:
        