class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close2open = {')':'(','}':'{',']':'['}
        if len(s) < 2:
            return False

        for p in s:
            if p in close2open.keys():
                if stack and stack[-1] == close2open[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return len(stack) == 0
        