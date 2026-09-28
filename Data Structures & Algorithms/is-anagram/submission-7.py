class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1) kind of brute force: O(2* n log n)
        # return sorted(s) == sorted(t)

        # 2) 2* hashmaps -> compare -> O(2n) time + constant space
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT


        