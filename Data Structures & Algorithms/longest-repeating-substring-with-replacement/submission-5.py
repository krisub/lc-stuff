class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        chars = defaultdict(int)
        left = 0
        chars[s[left]] += 1
        max_frq = s[left]
        max_len = 1

        for right in range(1, len(s), 1):
            chars[s[right]] += 1
            
            if chars[s[right]] > chars[max_frq]:
                max_frq = s[right]
            
            curr_substring_length = right - left + 1

            if curr_substring_length - chars[max_frq] > k:
                chars[s[left]] -= 1
                left += 1
            else:
                max_len = max(max_len, curr_substring_length)

        return max_len



