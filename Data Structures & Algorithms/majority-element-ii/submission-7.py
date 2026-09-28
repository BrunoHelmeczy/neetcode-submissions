class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 1) dict[nr, freq] -> if freq > len(nums) // 3 + 1 append to res
        count = {}
        res = set()
        m = (len(nums) // 3)
        for nr in nums:
            count[nr] = count.get(nr, 0) +1
        for nr in count.keys():
            if count[nr] > m:
                res.add(nr)

        return list(res)

        