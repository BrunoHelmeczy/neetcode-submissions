class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1) hashmap[str, list]: [sorted str, [original strs]] -> convert to list at end
        # pass
        anagram_map = defaultdict(list)

        for str_ in strs:
            key = ''.join(sorted(str_))

            if key not in anagram_map.keys():
                anagram_map[key] = [str_]
            else:
                anagram_map[key].append(str_)

        res = []

        for key, anagrams in anagram_map.items():
            res.append(anagrams)

        return res

        