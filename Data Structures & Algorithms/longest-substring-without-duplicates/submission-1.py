class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i= 0
        Max = 0
        for j in range(len(s)):
            while s[j] in s[i:j]:
                i+=1
            total  = j - i + 1
            Max = max(Max, total)
        return Max
            