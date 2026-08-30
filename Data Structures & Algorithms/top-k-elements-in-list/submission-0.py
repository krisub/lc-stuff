from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)

        for num in nums:
            count_dict[num] += 1

        output = sorted(count_dict, key=count_dict.get, reverse=True)

        return output[:k]
