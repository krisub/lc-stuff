import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        outputs = []
        for i in range(len(nums)):
            product = math.prod(nums[0:i])
            product *= math.prod(nums[i+1:])
            outputs.append(product)
        
        return outputs