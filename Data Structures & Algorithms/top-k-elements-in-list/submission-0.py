class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        freqs = [[] for i in range(len(nums)+1)]
        for nr in nums:
            count[nr] = 1+ count.get(nr, 0)
        for nr, freq in count.items():
            freqs[freq].append(nr)
        res =[]
        for c in range(len(freqs)-1,0, -1):
            for nr in freqs[c]:
                res.append(nr)
                if len(res)==k:
                    return res