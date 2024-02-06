class Solution(object):
    def groupAnagrams(self, strs):
        res = []
        mp = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            mp[sorted_str].append(s)

        for group in mp.values():
            res.append(group)

        return res
