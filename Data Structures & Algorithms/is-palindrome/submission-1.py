class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointers from end to centre
        # skip non alphanumeric characters
        # compare lower-case version

        i = 0
        j = len(s) - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            elif not s[j].isalnum():
                j -= 1
                continue
            elif s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
