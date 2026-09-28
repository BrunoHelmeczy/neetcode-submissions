class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        scounter, tcounter = {}, {}
        
        for i in range(len(s)):
            scounter[s[i]] = scounter.get(s[i], 0) +1
            tcounter[t[i]] = tcounter.get(t[i], 0) +1
        

        return scounter == tcounter