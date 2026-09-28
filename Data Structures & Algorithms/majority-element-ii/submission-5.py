class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 1) dict[nr, freq] -> if freq > len(nums) // 3 + 1 append to res
        count = {}
        res = set()
        for nr in nums:
            count[nr] = count.get(nr, 0) +1
        for nr in count.keys():
            if count[nr] >= ((len(nums) // 3) + 1):
                res.add(nr)

        return list(res)

        