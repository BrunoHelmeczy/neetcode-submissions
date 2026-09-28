class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = {}
        for w in strs:
            sortedw = ''.join(sorted(w))
            grps[sortedw] = grps.get(sortedw, []) + [w]

        return [grp for grp in grps.values()]

        
