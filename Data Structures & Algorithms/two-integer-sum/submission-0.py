from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[j] = target - nums[i]
        
        nums_set = defaultdict(int)

        # [3, 4, 5, 6], 7
        for i in range(len(nums)):
            diff = target - nums[i] # 4, 3, 2, 1
            if diff in nums_set: # 
                return [nums_set[diff], i]
            nums_set[nums[i]] = i # 3:0