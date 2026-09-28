class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # approaches
        # 1) sort s & t, compare: O(2 * n * log(n) + n) = Onlogn
        # 2) 2 frequency arrays (bucket sort); compare: return freq1 == freq2 O(2n) = O(n)
        # 3) 2 hashmaps; compare 
            # how to know which map is larger to compare against ?

        # 2) 2 freq arrays
        if len(s) != len(t):
            return False

        freq = [0] * 26

        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')] += 1
            freq[ord(t[i]) - ord('a')] -= 1

        for nr in freq:
            if nr != 0:
                return False
        return True
        