class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))

        # [2,20,4,10,3,4,5]
        # [2, 3, 4, 5, 10, 20]
        max_seq_len = 1
        curr_seq_len = 1
        for i in range(1, len(sorted_nums), 1):
            prev = sorted_nums[i-1]
            curr = sorted_nums[i]

            if curr == (prev + 1):
                curr_seq_len += 1
                if curr_seq_len > max_seq_len:
                    max_seq_len = curr_seq_len
            else:
                curr_seq_len = 1

        return max_seq_len