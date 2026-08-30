from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sublists = defaultdict(list) # (sorted letters, [word1, word2])

        for word in strs:
            key = ''.join(sorted(word))
            sublists[key].append(word)

        return list(sublists.values())
