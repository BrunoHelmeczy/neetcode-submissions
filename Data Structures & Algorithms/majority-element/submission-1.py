class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1) freq count map -> find key w max value
        count = {}
        for nr in nums:
            count[nr] = 1 + count.get(nr, 0)

        # max_nr = max(list(count.values()))
        max_count = 0
        for nr, cnt in count.items():
            max_count = max(max_count, cnt)

        for nr, cnt in count.items():
            if cnt == max_count:
                return nr
        
        # 2) boyer-moore algo
