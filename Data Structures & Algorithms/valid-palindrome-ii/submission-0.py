class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            l = 0
            r = len(s) - 1
            while l < r:
                if not s[l].isalnum():
                    l += 1
                    continue
                elif not s[l].isalnum():
                    r -= 1
                    continue
                elif s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            return True

        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[l].isalnum():
                r -= 1
                continue
            elif s[l].lower() != s[r].lower():
                return isPalindrome(s[(l + 1) : (r + 1)]) or isPalindrome(s[l:r])
            l += 1
            r -= 1
        return True


        