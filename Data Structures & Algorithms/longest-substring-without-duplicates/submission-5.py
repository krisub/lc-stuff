class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        if not s:
            return 0

        left = 0
        right = 1

        letters = set()
        letters.add(s[left])
        max_len = 1

        while left <= right and right < len(s):
            if left == right:
                letters.add(s[right])
                right += 1
            elif s[right] not in letters:
                letters.add(s[right])
                max_len = max(max_len, right - left + 1)
                right += 1
            else:
                letters.remove(s[left])
                left += 1

        return max_len
        '''

        if not s:
            return 0

        left = 0
        right = 1
        max_len = 1
        indexes = defaultdict(int)
        indexes[s[left]] = 0

        while right < len(s):
            if s[right] not in indexes or (s[right] in indexes and indexes[s[right]] < left):
                indexes[s[right]] = right
                max_len = max(max_len, right - left + 1)
            else: # s[right] is in indexes (s[right] = z, indexes[s[right]] is 0)
                left = indexes[s[right]] + 1
                indexes[s[right]] = right
            
            right += 1
                
        
        return max_len
        


