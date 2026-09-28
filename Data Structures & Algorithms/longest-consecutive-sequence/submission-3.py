class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1) sort asc; track res for longest streak; curr as 1st nr, streak as current streak, i 
        # 2) use set
        # track streak = current streak
        # track longest = max streak so far = max(longest, streak)
        # iterate over set nr_set elements nr
        # check if streak start w nr-1 in nr_set  

        num_set = set(nums)

        streak = longest = 0

        for nr in num_set:
            if (nr - 1) not in num_set:
                streak = 1
                while (nr + streak) in num_set:
                    streak += 1
            longest = max(longest, streak)
        return longest
        