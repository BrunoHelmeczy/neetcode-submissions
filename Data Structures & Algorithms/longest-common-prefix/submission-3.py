class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 1) sort strs -> compare 1st and last
        if len(strs) == 1:
            return strs[0]

        strs.sort()

        base = strs[0]
        comp = strs[-1]

        # if base is shorter, if we complete the check loop, we can return base only
        if len(base) > len(comp):
            base, comp = comp, base

        for i in range(len(base)):
            if base[i] != comp[i]:
                return base[:i]

        return base
