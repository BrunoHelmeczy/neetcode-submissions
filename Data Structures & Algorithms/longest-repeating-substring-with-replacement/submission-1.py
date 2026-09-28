class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 1) single pass - sliding window
        # chr freq dict
        # track length = nr characters in string
        l = res = maxfreq = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxfreq = max(maxfreq, count[s[r]])

            while (r - l + 1) - maxfreq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        
